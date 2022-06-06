from itertools import permutations
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
opt = list(map(int, input().split()))

opt_arr = ['+', '-', '*', '/']

opt_cnt = deque()
for i in range(len(opt)):
    for j in range(opt[i]):
        opt_cnt.append(opt_arr[i])

result = deque()

for i in permutations(opt_cnt, len(opt_cnt)):
    tmp = arr[0]
    for a, b in zip(arr[1:], i):
        if b == '+':
            tmp += a
        elif b == '-':
            tmp -= a
        elif b == '*':
            tmp *= a
        elif b == '/':
            if tmp < 0:
                tmp = (abs(tmp) // a) * -1
            else:
                tmp //= a
    result.append(tmp)

print(max(result))
print(min(result))
