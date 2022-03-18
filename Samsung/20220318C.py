def set_seat(student):
    global seat_arr,dx,dy,n,like_arr,arr
    like = -1
    empty = -1
    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            now_empty = 0
            now_like = 0
            if seat_arr[i][j] != 0:
             continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if ( nx < 0 or nx >= n or ny < 0 or ny >= n):
                    continue
                if seat_arr[nx][ny] == 0:
                    now_empty += 1
                elif seat_arr[nx][ny] in like_arr[student]: 
                    now_like += 1
            if like <= now_like:
                if like == now_like:
                    if empty <= now_empty:
                        x = i
                        y = j
                        like = now_like
                        empty = now_empty
                else:
                    x = i
                    y = j
                    like = now_like
                    empty = now_empty
            
          
    seat_arr[x][y] = arr[student]


n = int(input())
number = 0
dx = [1,0,0,-1]
dy = [0,-1,1,0]
result = 0
arr = [0]*(n*n)
like_arr = [[0]*5 for _ in range(n*n)]

for i in range(n*n):
    like_arr[i] = list(map(int, input().split()))

for i in range(n*n):
    arr[i] = like_arr[i][0]
    like_arr[i][0] = -1

seat_arr = [[0]*n for _ in range(n)]

seat = [[0]*n for _ in range(n)]

for i in range(n*n):
    set_seat(i)
    
for i in range(n):
    for j in range(n):
        seat[i][j] = seat_arr[n-1-i][n-1-j]        

for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if( nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            for l in range(n*n):
                if seat[i][j] == arr[l]:
                    number = l       
            if seat[nx][ny] in like_arr[number]:
                cnt += 1
        if cnt > 0:
            result += 10 ** (cnt-1)

print(result)


            
