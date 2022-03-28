# 치킨 배달

from itertools import combinations

n,m = map(int, input().split())
arr = []
for _ in range(n):
    num = list(map(int, input().split()))
    arr.append(num)

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            home.append((i,j))

chicken_lst = list(combinations(chicken, m))

ans = 1e9
result = []
for c in chicken_lst:
    home_dist = []
    for h in home:
        d = 1e9
        for i in range(m):
            dt = abs(h[0]-c[i][0]) + abs(h[1]-c[i][1])
            d = min(d, dt)
        home_dist.append(d)
        
    num = 0   
    for hd in home_dist:
        num += hd
    result.append(num)
    
ans = min(min(result), ans)
print(ans)
            
