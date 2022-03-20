n = int(input())

data = list(map(int, input().split()))
data.sort()
money = 1

for i in data:
    if money < i:
        break
    money += i    
    
print(money)
