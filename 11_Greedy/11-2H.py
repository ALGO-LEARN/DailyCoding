import sys
s = sys.stdin.readline().rstrip()
result = int(s[0])
for i in range(1, len(s)):
    tmp = int(s[i])
    if result <= 1 or tmp <= 1:
        result += tmp
    else:
        result *= tmp

print(result)