# BOJ 15683번: 감시
'''
도저히 구현을 못해서 답안지 보고 방향설정에서 비트마스킹, n진법 아이디어 확인함.
바킹독님 솔루션: https://blog.encrypted.gg/948
'''
dx = [1, 0, -1, 0] # 남, 동, 북, 서
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
grid1 = [list(map(int, input().split())) for _ in range(n)]
grid2 = [[0] * m for _ in range(n)]
cctv = []

def out_of_bounds(a, b):
    return a < 0 or a >= n or b < 0 or b >= m

def upd(x, y, d):
    d %= 4
    while True:
        x += dx[d]
        y += dy[d]
        if out_of_bounds(x, y) or grid2[x][y] == 6:
            return
        if grid2[x][y] != 0:
            continue
        grid2[x][y] = 7


count = 0
for i in range(n):
    for j in range(m):
        if grid1[i][j] != 0 and grid1[i][j] != 6:
            cctv.append((i, j))
        if grid1[i][j] == 0:
            count += 1
'''
2 * cctv 개수를 left shift를 한 이유는 cctv 1개당 4방향이기 때문에
1개라면, 4가지
2개라면, 4 * 4 = 16가지
3개라면, 4 * 4 * 4 = 64가지이다.

이 후, 방향에 대한 조합은 % 4(나머지연산), // 4(나눠서 몫 구하기)를 통해
4방향에 대한 인덱스(0인지 1인지 2인지 3인지)를 구해 해당 방향으로 탐색하러 갑니다.
(10진법의 자릿수 연산과 같은 논리)

나머지는 우리가 흔히 아는 일반적인 dfs 탐색 및 갯수 세기 로직과 동일하니 이런 특이케이스 아이디어는 배워갈만 하다 생각합니다.
ps. 랭커는 다름...;
'''
for tmp in range(1 << 2*len(cctv)):
    for i in range(n):
        for j in range(m):
            grid2[i][j] = grid1[i][j]
    brute = tmp
    for i in range(len(cctv)):
        _dir = brute % 4
        brute //= 4
        nx = cctv[i][0]
        ny = cctv[i][1]
        if grid1[nx][ny] == 1:
            upd(nx, ny, _dir)
        elif grid1[nx][ny] == 2:
            upd(nx, ny, _dir)
            upd(nx, ny, _dir+2)
        elif grid1[nx][ny] == 3:
            upd(nx, ny, _dir)
            upd(nx, ny, _dir+1)
        elif grid1[nx][ny] == 4:
            upd(nx, ny, _dir)
            upd(nx, ny, _dir+1)
            upd(nx, ny, _dir+2)
        elif grid1[nx][ny] == 5:
            upd(nx, ny, _dir)
            upd(nx, ny, _dir+1)
            upd(nx, ny, _dir+2)
            upd(nx, ny, _dir+3)
    val = 0
    for i in range(n):
        for j in range(m):
            if grid2[i][j] == 0:
                val += 1
    count = min(count, val)
print(count)
