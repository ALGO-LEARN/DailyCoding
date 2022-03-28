# 문자열 재정렬

import sys
input = sys.stdin.readline

s = input()
alpha = []
number = []

for i in range(len(s)-1):
    if s[i].isalpha() == True:
        alpha.append(s[i])
    else:
        number.append(int(s[i]))

alpha.sort()
result = alpha + [str(sum(number))]
print(''.join(result))
