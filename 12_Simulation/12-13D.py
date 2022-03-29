from itertools import combinations

n, m = map(int, input().split())
home, chick = [], []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            chick.append([i, j])
        if tmp[j] == 1:
            home.append([i, j])

able = list(combinations(chick, m))
result = int(1e9)   # 전체 중에 최소를 구하는 것

for x in able:
    street = 0   # 해당되는 좌표 중 최소를 구하는 것
    for a in home:
        least = int(1e9)
        for y in x:
            tmp = abs(a[0] - y[0]) + abs(a[1] - y[1])
            least = min(least, tmp)
        street += least
    result = min(result, street)
print(result)
