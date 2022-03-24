# 좌물쇠와 열쇠

import copy

def solution(key, lock):
    # 2차원 배열(key) 90도 회전
    # 열-> |((n-1)-행)|, 행-> 열
    def rotate(k):
        rotate_key = [ [0] * len(k) for _ in range(len(k))]
        for i in range(len(k)):
            for j in range(len(k)):
                rotate_key[i][j] = k[j][abs(len(k)-1-i)]
        return rotate_key

    # 새로운 자물쇠 배열 선언
    result = False
    arr = [ [1] * (len(lock) + (len(key)-1)*2) for _ in range(len(lock) + (len(key)-1)*2)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            arr[i+len(key)-1][j+len(key)-1] = lock[i][j]
    
    # 완전탐색
    for _ in range(4):
        key = rotate(key)
        for i in range(len(arr)-(len(key)-1)):
            for j in range(len(arr)-(len(key)-1)):
                new_lock = copy.deepcopy(arr)

                # 자물쇠와 키의 값의 합산
                for k1 in range(len(key)):
                    for k2 in range(len(key)):
                        new_lock[i+k1][j+k2] = new_lock[i+k1][j+k2] + key[k1][k2]
                
                # new_lock의 자물쇠부분 확인
                cnt = 0
                for l1 in range(len(lock)):
                    for l2 in range(len(lock)):
                        if new_lock[l1+len(key)-1][l2+len(key)-1] == 1:
                            cnt+=1         
                if cnt == len(lock)*len(lock):
                    result = True
                    return result
    return result
