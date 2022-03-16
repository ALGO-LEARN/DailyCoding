arr = input()
tmp = arr[0]
n_arr = [tmp]

for i in arr:
    if tmp != i:
        tmp = i
        n_arr.append(tmp)

print(min(n_arr.count('0'), n_arr.count('1')))
