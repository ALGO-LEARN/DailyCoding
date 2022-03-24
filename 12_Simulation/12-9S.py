# 문자열 압축 

def solution(s):
    result = 1e9
    
    def divide(list, n):
        arr = []
        for i in range(0, len(list), n):
            arr.append(list[i:i+n])
        return arr
    
    for step in range(1, len(s) // 2 + 2):
        cnt = 1
        answer = ''
        arr = divide(s, step)
        num = arr[0]
        for i in range(1, len(arr)):
            if num == arr[i]:
                cnt += 1
            else:
                if cnt >= 2:  
                    a = str(cnt) + str(num)
                    answer += a
                    cnt = 1
                    num = arr[i] 
                else:   
                    answer += num
                    cnt = 1
                    num = arr[i] 
        answer += str(cnt) + num if cnt >= 2 else num
        result = min(result, len(answer))
        answer = ''
    
    return result
