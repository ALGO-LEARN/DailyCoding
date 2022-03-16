n = int(input())
num = list(map(int, input().split()))
num.sort

ans = 0
cnt = 0

for i in num:
    cnt += 1
    if cnt >= i:
        ans += 1
        cnt = 0

print(ans)