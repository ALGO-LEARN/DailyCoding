# BOJ 21608번: 상어 초등학교
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
n_square = n ** 2
students = [list(map(int, input().split())) for _ in range(n_square)]

arr = [[0] * n for _ in range(n)]

for s in range(n_square):
    tmp = []
    for i in range(n):
        for j in range(n):
            sumLike, sumEmpty = 0, 0
            if arr[i][j] != 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                    continue
                if arr[nx][ny] in students[s][1:]:
                    sumLike += 1
                if arr[nx][ny] == 0:
                    sumEmpty += 1
            tmp.append((sumLike, sumEmpty, (i, j)))
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2]))

    arr[tmp[0][2][0]][tmp[0][2][1]] = students[s][0]

# print(arr)
# print(students)

likes = {}
for i in range(n_square):
    tmp = students[i][0]
    likes[tmp] = students[i][1:]

# print(likes)
result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            if arr[nx][ny] in likes[arr[i][j]]:
                cnt += 1
                continue
        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)