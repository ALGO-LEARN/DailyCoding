N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

_max = -1e9
_min = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global _max, _min
    if depth == N:
        _max = max(total, _max)
        _min = min(total, _min)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(_max)
print(_min)
