def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        result = ""
        tmp = s[0:i]
        count = 1
        
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                count += 1
            else:
                result += str(count) + tmp if count >= 2 else tmp
                tmp = s[j:j+i]
                count = 1
                
        result += str(count) + tmp if count >= 2 else tmp
        answer = min(answer, len(result))
    return answer