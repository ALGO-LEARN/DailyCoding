def solution(food_times, k):
    # 합이 0이면 할 필요 없음
    if k >= sum(food_times):
        return -1
    # [[2번, 1], [3번, 2], [1번, 3]] 구조, 오름차순
    times_sorted = sorted([(idx+1, val) for idx, val in enumerate(food_times)], key=lambda x: x[1])
    idx = 0                     # 0은 제외한 이후 배열을 위한 인덱스
    n = len(food_times)         # 배열 최대 길이
    cycle = times_sorted[0][1]  # 첫 사이클

    while k-(n*cycle) > 0:      # 오류 난 k 전까지
        k -= n*cycle            # 우선 사이클 단위로 빼고
        n -= 1                  # 0은 pass
        idx += 1                # 한 칸씩 앞으로
        cycle = times_sorted[idx][1]-times_sorted[idx-1][1] # 사이클 계산

    return [i[0] for i in sorted(times_sorted[idx:])][k % n] # 위치 계산
