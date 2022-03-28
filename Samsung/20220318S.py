# 2022.03.18 상어초등학교
# 알고리즘 스터디 1주차

n = int(input())
arr = [[0]*n for _ in range(n)]

student = []
for _ in range(n*n):
    m = list(map(int, input().split()))
    student.append(m)

dx = [1,-1,0,0]
dy = [0,0,-1,1]
    
# 계산
for s in student:
    s1 = s[0]
    s2 = s[1:]
    maps= [] # 계산완료된 것
    
    for i in range(n):
        for j in range(n):
            # 첫번째 두번째
            cnt_1 = 0
            cnt_2 = 0
            
            if arr[i][j] != 0:
                continue
            
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or x >= n or y < 0 or y >= n:
                    continue
                if arr[x][y] in s2:
                    cnt_1 += 1
                elif arr[x][y] == 0:
                    cnt_2 += 1
            maps.append([cnt_1, cnt_2, i, j])
            
##    print('이전의 maps', maps)
    # 좋아하는 학생이 인접한 수, 인접한칸중 비어있는칸수, 행, 열 순
    maps.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))
##    print('maps',maps)
    data = maps[0]
##    print('data',data)
    arr[data[2]][data[3]] = s1
##    print('arr',arr)
##    print()  
                
# 만족도구하기
result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            for s3 in student:
                if arr[i][j] == s3[0]:
                    if arr[x][y] in s3[1:]:
                        cnt+=1
                        
        if cnt == 0:
            result += 0
        elif cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000
print(result)

