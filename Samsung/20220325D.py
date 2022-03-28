# Successed code
import copy
n, m = map(int, input().split())
cctv = []
graph = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, graph)
print(min_value)

# Failed code
"""
"n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def checker(cnt, tmp, cnt_arr, tmp_arr):
    if cnt < tmp:
        return tmp, tmp_arr
    else:
        return cnt, cnt_arr


def left(x, y):
    tmp, tmp_arr = 0, []
    for k in range(y - 1, -1, -1):
        if k < 0:
            break
        if arr[x][k] == 0:
            tmp_arr.append([x, k])
            tmp += 1
        elif arr[x][k] == 6:
            break
    return tmp, tmp_arr


def right(x, y):
    tmp, tmp_arr = 0, []
    for k in range(y + 1, m):
        if k >= m:
            break
        if arr[x][k] == 0:
            tmp_arr.append([x, k])
            tmp += 1
        elif arr[x][k] == 6:
            break
    return tmp, tmp_arr


def top(x, y):
    tmp, tmp_arr = 0, []
    for k in range(x - 1, -1, -1):
        if k < 0:
            break
        if arr[k][y] == 0:
            tmp_arr.append([k, y])
            tmp += 1
        elif arr[k][y] == 6:
            break
    return tmp, tmp_arr


def bottom(x, y):
    tmp, tmp_arr = 0, []
    for k in range(x + 1, n):
        if k >= n:
            break
        if arr[k][y] == 0:
            tmp_arr.append([k, y])
            tmp += 1
        elif arr[k][y] == 6:
            break
    return tmp, tmp_arr


def cam1(i, j):
    cnt, cnt_arr = 0, []

    tmp, tmp_arr = left(i, j)
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = right(i, j)
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = top(i, j)
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = bottom(i, j)
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    for x, y in cnt_arr:
        arr[x][y] = '#'


def cam2(i, j):
    cnt, cnt_arr = 0, []

    tmp, tmp_arr = left(i, j)
    tmp1, tmp_arr1 = right(i, j)
    tmp += tmp1
    tmp_arr += tmp_arr1
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = top(i, j)
    tmp1, tmp_arr1 = bottom(i, j)
    tmp += tmp1
    tmp_arr += tmp_arr1
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    for x, y in cnt_arr:
        arr[x][y] = '#'


def cam3(i, j):
    cnt, cnt_arr = 0, []
    tmp, tmp_arr = left(i, j)
    tmp1, tmp_arr1 = top(i, j)
    tmp += tmp1
    tmp_arr += tmp_arr1
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = right(i, j)
    tmp1, tmp_arr1 = bottom(i, j)
    tmp += tmp1
    tmp_arr += tmp_arr1
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    for x, y in cnt_arr:
        arr[x][y] = '#'


def cam4(i, j):
    cnt, cnt_arr = 0, []

    tmp, tmp_arr = left(i, j)
    tmp1, tmp_arr1 = top(i, j)
    tmp2, tmp_arr2 = right(i, j)
    tmp = tmp + tmp1 + tmp2
    tmp_arr = tmp_arr + tmp_arr1 + tmp_arr2
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = top(i, j)
    tmp1, tmp_arr1 = right(i, j)
    tmp2, tmp_arr2 = bottom(i, j)
    tmp = tmp + tmp1 + tmp2
    tmp_arr = tmp_arr + tmp_arr1 + tmp_arr2
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = left(i, j)
    tmp1, tmp_arr1 = bottom(i, j)
    tmp2, tmp_arr2 = right(i, j)
    tmp = tmp + tmp1 + tmp2
    tmp_arr = tmp_arr + tmp_arr1 + tmp_arr2
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    tmp, tmp_arr = left(i, j)
    tmp1, tmp_arr1 = top(i, j)
    tmp2, tmp_arr2 = bottom(i, j)
    tmp = tmp + tmp1 + tmp2
    tmp_arr = tmp_arr + tmp_arr1 + tmp_arr2
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    for x, y in cnt_arr:
        arr[x][y] = '#'


def cam5(i, j):
    cnt, cnt_arr = 0, []
    tmp, tmp_arr = left(i, j)
    tmp1, tmp_arr1 = right(i, j)
    tmp2, tmp_arr2 = top(i, j)
    tmp3, tmp_arr3 = bottom(i, j)
    tmp = tmp + tmp1 + tmp2 + tmp3
    tmp_arr = tmp_arr + tmp_arr1 + tmp_arr2 + tmp_arr3
    cnt, cnt_arr = checker(cnt, tmp, cnt_arr, tmp_arr)

    for x, y in cnt_arr:
        arr[x][y] = '#'


for a in range(n):
    for b in range(m):
        if arr[a][b] == 1:
            cam1(a, b)
        elif arr[a][b] == 2:
            cam2(a, b)
        elif arr[a][b] == 3:
            cam3(a, b)
        elif arr[a][b] == 4:
            cam4(a, b)
        elif arr[a][b] == 5:
            cam5(a, b)

ans = 0
for i in arr:
    for j in i:
        if j == 0:
            ans += 1

print(ans)
"""
