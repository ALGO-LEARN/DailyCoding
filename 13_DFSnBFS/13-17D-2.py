import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nxt_dict = {i: [] for i in range(1, k+1)}
board = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] > 0:
            nxt_dict[tmp[j]].append([i, j])
    board.append(tmp)
s, x, y = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(idx, arr):
    return_arr = []
    while arr:
        ax, ay = arr.pop()
        for a in range(4):
            bx = ax + dx[a]
            by = ay + dy[a]

            if 0 <= bx < n and 0 <= by < n and board[bx][by] == 0:
                return_arr.append([bx, by])
                board[bx][by] = idx

    return return_arr


for _ in range(s):
    for i, j in nxt_dict.items():
        nxt_dict[i] = bfs(i, j)

print(board[x-1][y-1])
