arr = list(map(int, list(input())))
_max = arr[0]

for i in range(1, len(arr)):
    _max = max(_max+arr[i], _max*arr[i])

print(_max)
