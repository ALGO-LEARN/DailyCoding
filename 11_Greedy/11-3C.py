n = input()
one = 0
zero = 0
compare = n[0]

for i in range(1, len(n)-1):
    if n[i+1] != compare:
        if compare == '0':
            compare = '1'
            zero += 1
        else:
            compare = '0'
            one += 1
print( one if one > zero else zero)
