# BOJ 15686번: 치킨 배달
from itertools import combinations
# 1: 집, 2: 치킨집
def dist(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
homes, chickens = [], []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append((i, j))
        if city[i][j] == 2:
            chickens.append((i, j))

result = 1e9
for com in combinations(chickens, m): # 치킨집들 중 m개만 선택한 조합 리스트
    # print(com, end=": ")
    tmp = 0
    for hx, hy in homes:
        min_val = 1e9
        for cx, cy in com:
            distance = dist(hx, hy, cx, cy)
            min_val = min(min_val, distance)
        tmp += min_val
    #     print(min_val, end=" ")
    # print(tmp)
    result = min(result, tmp)

print(result)
