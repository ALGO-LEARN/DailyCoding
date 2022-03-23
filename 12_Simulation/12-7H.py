# BOJ 18406번: 럭키 스트레이트
n = input()
length = len(n) // 2

first, second = 0, 0
for i in range(length):
    first += int(n[i])
for i in n[-1:length-1:-1]:
    second += int(i)

if first == second:
    print("LUCKY")
else:
    print("READY")