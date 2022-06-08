from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
K = 0


def bfs(ix, jx, visited):
    deq = deque()
    deq.append([ix, jx])

    union = set()
    union.add((ix, jx))

    visited[ix][jx] = 1
    sum_ = board[ix][jx]
    while deq:
        x, y = deq.popleft()
        for a in range(4):
            nx = dx[a] + x
            ny = dy[a] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(board[nx][ny]-board[x][y]) <= r:
                sum_ += board[nx][ny]
                union.add((nx, ny))
                deq.append([nx, ny])
                visited[nx][ny] = 1

    if len(union) == 1:
        return False, False
    return union, sum_


while K < 2000:

    visited = [[0]*n for _ in range(n)]
    union_arr = []
    sum_arr = []
    for i in range(n):
        for j in range(n):
            u, s = bfs(i, j, visited)
            if u and s:
                union_arr.append(u)
                sum_arr.append(s)

    if not union_arr:
        print(K)
        break

    for i, j in zip(union_arr, sum_arr):
        tmp_ans = j // len(i)
        for k in i:
            board[k[0]][k[1]] = tmp_ans

    K += 1
