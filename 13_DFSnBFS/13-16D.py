from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
board = []
free = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if not tmp[j]:
            free.append([i, j])    # 0인 구역 구하기
    board.append(tmp)

able = list(combinations(free, 3)) # 가능한 모든 경우의 수 구하기

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    deq = deque([[x, y]])
    while deq:
        nx, ny = deq.popleft()

        for i in range(4):
            tx = nx + dx[i]
            ty = ny + dy[i]

            if 0 <= tx < N and 0 <= ty < M and not visited[tx][ty] and not c_board[tx][ty]:
                deq.append([tx, ty])
                c_board[tx][ty] = 2
                visited[tx][ty] = 1


ans = 0
for k in able:
    c_board = copy.deepcopy(board)
    visited = [[0]*M for _ in range(N)]

    for s in k:
        c_board[s[0]][s[1]] = 1

    for i in range(N):
        for j in range(M):
            if c_board[i][j] == 2 and not visited[i][j]:
                bfs(i, j)
    tmp = 0
    for zero in c_board:
        tmp += zero.count(0)
    ans = max(ans, tmp)

print(ans)

