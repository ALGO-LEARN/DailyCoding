# BOJ 1439번: 뒤집기
import sys
input = sys.stdin.readline()
s = input.rstrip()
toOne = 0
toZero = 0
for i in range(1, len(s)):
    if s[i] != s[i-1] and s[i-1] == '0':
        toOne += 1
    elif s[i] != s[i-1] and s[i-1] == '1':
        toZero += 1

if s[-1] == '0':
    toOne += 1
else:
    toZero += 1

print(min(toOne, toZero))