# 모험가길드

N = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0   # 총 그룹의 수
group = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:
    group += 1
    if group >= i:
        result += 1
        group = 0

print(result)
