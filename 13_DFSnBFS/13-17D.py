from sys import stdin
from collections import deque

N, K = map(int, input().split())
board = []
k_arr = [deque() for _ in range(K+1)]

for i in range(N):
    tmp = list(map(int, stdin.readline().split()))
    for j, k in enumerate(tmp):
        if k:
            k_arr[k].append([i, j])
    board.append(tmp)

S, X, Y = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def wave(arr, v):
    fix = deque()
    while arr:
        x, y = arr.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                if v == board[x][y]:
                    board[nx][ny] = v
                    fix.append([nx, ny])
    return fix


def bfs():
    for i in range(1, K+1):
        k_arr[i] = wave(k_arr[i], i)


for _ in range(S):
    bfs()

print(board[X-1][Y-1])
