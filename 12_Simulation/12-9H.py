def solution(s):
    answer = len(s)
    for n in range(1, len(s)//2+1): # 압축 단위를 1개부터 점차 늘려가며 확인
        result = ""
        count = 1
        tmp = s[0:n] # 단위 문자열 초기화
        for i in range(n, len(s), n): # 단위 크기만큼 증가시키며 이전 문자열과 비교
            if tmp == s[i:i+n]: # 이전 상태와 동일하다면 count 증가
                count += 1
            else: # 다른 문자열이 나온 경우
                if count == 1:
                    result += tmp
                else:
                    result += str(count) + tmp
                tmp = s[i:i+n] # 상태 초기화
                count = 1
        result += str(count) + tmp if count >= 2 else tmp # 남아있는 문자열에 대한 처리
        answer = min(answer, len(result))
    return answer

# Test Case
s1 = "aabbaccc"
print(solution(s1))

s2 = "ababcdcdababcdcd"
print(solution(s2))

s3 = "abcabcdede"
print(solution(s3))

s4 = "abcabcabcabcdededededede"
print(solution(s4))

s5 = "xababcdcdababcdcd"
print(solution(s5))
