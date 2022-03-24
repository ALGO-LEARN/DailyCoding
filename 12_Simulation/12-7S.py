# 럭키 스트레이트

n = input()
length = int(len(n)/2)

first = n[:length]
second = n[length:]
result = [0,0]
for i in range(len(first)):
    result[0] += int(first[i])
    result[1] += int(second[i])

if result[0] == result[1]:
    print('LUCKY')
else:
    print('READY')
