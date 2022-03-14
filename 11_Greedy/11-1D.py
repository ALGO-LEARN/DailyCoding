from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans, count = 0, 0

for i in sorted(arr):
    count += 1
    if i == count:
        ans += 1
        count = 0

print(ans)
