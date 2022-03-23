n = input()
m = len(n)//2
print("LUCKY") if sum(list(map(int, n[:m]))) == sum(list(map(int, n[m:]))) else print("READY")
