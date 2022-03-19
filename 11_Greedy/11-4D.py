input()

ans = 1
for i in sorted(list(map(int, input().split()))):
    if ans >= i:
        ans += i
    else:
        print(ans)
        break
