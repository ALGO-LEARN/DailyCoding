N = int(input())
board = [input().split() for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0


def dfs(r, c, cnt):
    global answer
    if cnt == 3:
        yes = True

        for i in range(N):
            for j in range(N):
                if board[i][j] != 'T':
                    continue
                if findS(i, j):
                    yes = False
                    break
            if not yes:
                break
        if yes:
            answer = 1
        return

    for i in range(c+1, N):
        if board[r][i] != 'X':
            continue

        board[r][i] = 'O'
        dfs(r, i, cnt + 1)
        board[r][i] = 'X'

    for i in range(r+1, N):
        for j in range(N):
            if board[i][j] != 'X':
                continue
            board[i][j] = 'O'
            dfs(i, j, cnt + 1)
            board[i][j] = 'X'


def findS(r, c):
    for i in range(4):
        nextR = r
        nextC = c
        while True:
            nextR += dx[i]
            nextC += dy[i]
            if 0 > nextR or nextR >= N or 0 > nextC or nextC >= N:
                break
            if board[nextR][nextC] == 'O':
                break
            if board[nextR][nextC] == 'S':
                return True

    return False


dfs(0, -1, 0)
print("YES") if answer == 1 else print("NO")

