# 곱하기혹은더하기

N = input()

result = 0
for v in N:
    if (v == '0') or (v=='1'):
        result += int(v)
    else:
        if result == 0:
            result += int(v)
        else:
            result *= int(v)
print(result)
