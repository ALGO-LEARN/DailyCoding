# 만들수없는금액

from itertools import permutations

n = int(input())
data = list(map(int, input().split()))

# 순열 라이브러리를사용하여 모든 조합의 경우 구하기
chk = []
result = []
for i in range(1, n):
    chk = list(permutations(data,i))
    for j in range(len(chk)):
        result.append(sum(chk[j]))
        
# set으로 중복제거
result = set(result)
result = list(result)
result.sort()

# 비교
cnt = 1
for v in result:
    if cnt < v:
        print(cnt)
        break
    else:
        cnt += 1



