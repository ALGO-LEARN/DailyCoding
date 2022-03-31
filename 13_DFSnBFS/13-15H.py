# BOJ 18352번: 특정 거리의 도시 찾기
from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
nodes = [[] for _ in range(n+1)]
dist = [-1] * (n+1)
dist[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)

queue = deque()
queue.append(x)
while queue:
    cur = queue.popleft()
    for next_node in nodes[cur]:
        if dist[next_node] == -1:
            dist[next_node] = dist[cur] + 1
            queue.append(next_node)

for i in range(n+1):
    if dist[i] == k:
        print(i)

if k not in dist:
    print(-1)