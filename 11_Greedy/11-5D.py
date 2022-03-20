input()
arr = list(map(int, input().split()))
cnt = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] != arr[j]:
            cnt += 1

print(cnt)
