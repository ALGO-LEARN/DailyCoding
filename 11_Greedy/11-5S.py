# 볼링공 고르기

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 조합 라이브러리를 사용하여 해당 조합의 경우 구하기
result = list(combinations(data,2))
for i in range(len(result)):
    result[i] = list(result[i])

# 같은 무게를 고른경우 제거
for idx, v in enumerate(result):
    if v[0] == v[1]:
        del result[idx]
print(len(result))

