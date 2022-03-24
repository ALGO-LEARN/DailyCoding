n = input()
half = len(n)//2

left = 0 
right = 0

for i in range(0,int(half)):
    left += int(n[i])
for j in range(half,len(n)):
    right += int(n[j])

if left == right:
    print("LUCKY")
else:
    print("READY")