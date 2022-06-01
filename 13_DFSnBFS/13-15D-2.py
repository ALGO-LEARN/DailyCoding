from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
dic = {i: [] for i in range(1, n+1)}
for _ in range(m):
    i, j = map(int, input().split())
    dic[i].append(j)

que = deque([[x, 0]])

visited = [0 for _ in range(n+1)]
visited[x] = 1
while que:
    node, depth = que.popleft()
    if depth == k:
        que.appendleft([node, depth])
        break
    for i in dic[node]:
        if not visited[i]:
            que.append([i, depth+1])
            visited[i] = 1

arr = []
if que:
    for i in que:
        if i[1] == k:
            arr.append(i[0])

    for i in sorted(arr):
        print(i)

else:
    print(-1)

