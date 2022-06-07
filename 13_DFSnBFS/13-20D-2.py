from itertools import combinations
import copy

n = int(input())
teacher, board = [], []
able_block = []

for i in range(n):
    tmp = input().split()
    for j, k in enumerate(tmp):
        if k == 'T':
            teacher.append([i, j])
        elif k == 'X':
            able_block.append([i, j])
    board.append(tmp)

result = False

for able in combinations(able_block, 3):
    temp = copy.deepcopy(board)
    for a in able:
        temp[a[0]][a[1]] = 'O'
    result_cnt = True
    for b in teacher:
        for tmp_x in range(b[0], -1, -1):
            if temp[tmp_x][b[1]] == 'O':
                result_cnt = True
                break
            elif temp[tmp_x][b[1]] == 'S':
                result_cnt = False
                break
        if not result_cnt: break;
        for tmp_x in range(b[0], n):
            if temp[tmp_x][b[1]] == 'O':
                result_cnt = True
                break
            elif temp[tmp_x][b[1]] == 'S':
                result_cnt = False
                break
        if not result_cnt: break;
        for tmp_y in range(b[1], -1, -1):
            if temp[b[0]][tmp_y] == 'O':
                result_cnt = True
                break
            elif temp[b[0]][tmp_y] == 'S':
                result_cnt = False
                break
        if not result_cnt: break;
        for tmp_y in range(b[1], n):
            if temp[b[0]][tmp_y] == 'O':
                result_cnt = True
                break
            elif temp[b[0]][tmp_y] == 'S':
                result_cnt = False
                break
        if not result_cnt: break;
    if result_cnt:
        print("YES")
        result = True
        break

if not result:
    print("NO")
