# 뱀
from collections import deque

# 방향전환 함수
def transfer_direction(p, d):
    right = [3,1,2,0]  # 우,하,좌,상
    left = [3,0,2,1]  # 우,상,좌,하
    if d == 'L':
        idx = left.index(p)
        idx = (idx+1) % 4
        p = left[idx]  
    else:
        idx = right.index(p)
        idx = (idx+1) % 4
        p = right[idx] 
    return p

# 입력
n = int(input())
arr = [ [0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    num = list(map(int, input().split()))
    arr[num[0]-1][num[1]-1] = 1  # 사과위치
    
x = int(input())
d_arr = []
for _ in range(x):
    num2 = list(input().split())
    d_arr.append((int(num2[0]),num2[1]))
    
# 구현
i = 0
dnt = 0     # 방향인덱스
dx = [-1,1,0,0]   # 상,하,좌,우
dy = [0,0,-1,1]
p = 3       # 현재방향
snake = deque()

while True:
    if i == 0:
        arr[0][0] = 2
        snake.append((0,0))
        x = 0
        y = 0
        
    else:
        x = x + dx[p]
        y = y + dy[p]
        if x < 0 or x >= n or y < 0 or y >= n or arr[x][y] == 2:
            break
        
        if arr[x][y] == 1:
            snake.append((x,y))
            arr[x][y] = 2
        else:
            snake.append((x,y))
            arr[x][y] = 2
            s = snake.popleft()
            arr[s[0]][s[1]] = 0

        if dnt < len(d_arr):
            if i == d_arr[dnt][0]:
                if d_arr[dnt][1] == 'L':
                    p = transfer_direction(p,'L')
                else:
                    p = transfer_direction(p,'R')
                dnt+=1 
    i+=1
print(i)
     
