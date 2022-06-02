from itertools import combinations
import copy
from collections import deque
import sys

# input = sys.stdin.readline

n, m = map(int, input().split())
board = []
zero_arr = []
virus_arr = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            zero_arr.append([i, j])
        elif tmp[j] == 2:
            virus_arr.append([i, j])
    board.append(tmp)

able = list(combinations(zero_arr, 3))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_ = 0

for a in able:
    tmp_board = copy.deepcopy(board)
    que = deque(virus_arr)

    for b in a:
        tmp_board[b[0]][b[1]] = 1

    while que:
        pos_x, pos_y = que.popleft()

        for i in range(4):
            x = pos_x + dx[i]
            y = pos_y + dy[i]

            if 0 <= x < n and 0 <= y < m and not tmp_board[x][y]:
                que.append([x, y])
                tmp_board[x][y] = 2

    count_tmp = 0
    for i in tmp_board:
        count_tmp += i.count(0)

    max_ = max(max_, count_tmp)

print(max_)
