from collections import deque

n = int(input())
board = [[0]*n for _ in range(n)]

for _ in range(int(input())):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

times = {}
for _ in range(int(input())):
    i, j = input().split()
    times[int(i)] = j

way = [[0, -1], [-1, 0], [0, 1], [1, 0]]


def start():
    position = 2  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    board[y][x] = 2
    while True:
        y, x = y + way[position][0], x + way[position][1]
        if 0 <= y < n and 0 <= x < n and board[y][x] != 2:
            if not board[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                board[temp_y][temp_x] = 0  # 꼬리 제거
            board[y][x] = 2
            visited.append([y, x])

            if time in times.keys():
                position = (position-1) % 4 if times[time] == 'L' else (position+1) % 4

            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


print(start())
