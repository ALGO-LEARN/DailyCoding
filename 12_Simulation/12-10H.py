def rotate(arr):
    row = len(arr)
    col = len(arr[0])
    new_arr = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_arr[j][row - i - 1] = arr[i][j]
    return new_arr

def count(new_lock):
    length = len(new_lock) // 3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if count(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
        return False

# Test Case
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))