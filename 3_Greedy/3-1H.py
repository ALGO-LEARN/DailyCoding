n = int(input())
coins = [500, 100, 50, 10]
answer = 0
for i in coins:
    answer += n // i
    n %= i
print(answer)