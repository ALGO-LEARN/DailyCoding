def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))
    foods.sort()
    preTime = 0
    for i, food in enumerate(foods):
        diff = food[0] - preTime
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                preTime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key=lambda x: x[1])
                return sublist[k][1]
        n -= 1
    return -1

# Test Case 1
food_times1 = [3, 1, 2]
k1 = 5
print(solution(food_times1, k1))

# Test Case 2
food_times2 = [3, 5, 1, 6, 5, 3]
k2 = 20
print(solution(food_times2, k2))