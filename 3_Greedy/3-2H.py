n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
count = (int(m / (k + 1)) * k) + (m % (k + 1))

result = 0
result += count * arr[-1]
result += (m - count) * arr[-2]

print(result)

''' Test Case
5 8 3
2 4 5 4 6
'''