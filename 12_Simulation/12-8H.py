s = input()
arr = []
tmp = 0
for i in range(len(s)):
    if s[i].isalpha():
        arr.append(s[i])
    elif s[i].isdigit():
        tmp += int(s[i])

arr.sort()
arr.append(tmp)

for i in arr:
    print(i, end='')

# Test Case 1: K1KA5CB7
# Test Case 2: AJKDLSI412K4JSJ9D