# BOJ 3190번: 뱀
from collections import deque
dx = [0, 1, 0, -1] # 동, 남, 서, 북
dy = [1, 0, -1, 0]

def rotate(dir, c):
    if c == 'L':
        direction = (dir - 1) % 4
    else:
        direction = (dir + 1) % 4
    return direction

N = int(input())
board = [[0] * (N+1) for _ in range(N+1)] # 1, 1 부터 N, N 까지

K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 1

L = int(input())
info = []
for _ in range(L):
    x, c = input().split() # X초, C방향(L or D)
    info.append((int(x), c))

time = 0
dir = 0
info_index = 0
x, y = 1, 1
board[x][y] = 2
queue = deque()
queue.append((x, y))
while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
        if board[nx][ny] == 0: # 사과 x
            board[nx][ny] = 2
            cur_x, cur_y = queue.popleft()
            board[cur_x][cur_y] = 0
            queue.append((nx, ny))
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            queue.append((nx, ny))
    else:
        time += 1
        break
    x, y = nx, ny
    time += 1
    if info_index < L and info[info_index][0] == time:
        dir = rotate(dir, info[info_index][1])
        info_index += 1

print(time)