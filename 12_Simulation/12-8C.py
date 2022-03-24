n = input()
alpha = []
number = 0

for i in range(len(n)):
    if n[i].isalpha():
        alpha.append(n[i])
    else:
        number += int(n[i])
alpha.sort()
alpha.append(number)
result = ''.join(str(s) for s in alpha)
print(result)
