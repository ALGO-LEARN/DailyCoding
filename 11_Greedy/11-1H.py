import sys
a = int(sys.stdin.readline().rstrip())
worried = list(map(int, sys.stdin.readline().split()))
worried.sort()
answer, count = 0, 0
for i in worried:
    count += 1
    if count == i:
        answer += 1
        count = 0
print(answer)