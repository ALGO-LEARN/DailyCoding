# 2022/03/18, Samsung Coding Test
# https://www.acmicpc.net/problem/21608

import sys

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
N = int(input())
arr = [[0] * N for _ in range(N)]

likeDict = {}
result = 0

for _ in range(N * N):
    _input = list(map(int, input().split()))    # 한 줄 받을 때
    likeDict[_input[0]] = _input[1:]            # 딕셔너리 타입으로 변환

    max_x, max_y = 0, 0                         # 각 학생 근접 순회할 때 가장 최적의 위치 x, y
    max_like, max_empty = -1, -1                # 최적 위치를 구하기 위해 각 순회구간마다 최대를 저장하는 변수들

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:                  # 전제조건은 아직 비어있는 곳
                likeCnt, emptyCnt = 0, 0        # 각 순간마다 최대를 저장하는 변수들

                for k in range(4):              # 상 하 좌 우 bfs 특징
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] in _input[1:]:   # 각 학생마다 좋아하는 친구들
                            likeCnt += 1
                        elif arr[nx][ny] == 0:          # 학생이 좋아하는 친구가 근처에 없을 때
                            emptyCnt += 1
                # 근처에 좋아하는 친구 한명이라도 있거나 빈 배열 순회할 때 값을 max_like를 업데이트.
                if max_like < likeCnt or (max_like == likeCnt and max_empty < emptyCnt):
                    max_x = i
                    max_y = j
                    max_like = likeCnt
                    max_empty = emptyCnt

    arr[max_x][max_y] = _input[0]   # 순회 마무리 될 때 결과가 저장됨

for i in range(N):
    for j in range(N):
        cnt = 0                     # 주변에 있는 친구 수 세기
        like = likeDict[arr[i][j]]  # 좋아하는 친구 배열
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] in like:
                    cnt += 1
        if cnt != 0:                    # 친구가 있는 상황에만 더하기
            result += 10 ** (cnt - 1)   # 문제 특성상 10^n으로 해결 가능함

print(result)
