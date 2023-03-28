# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    perfos = list(map(int, input().split()))
    foods = list(map(int, input().split()))

    perfos.sort(reverse=True)
    foods.sort()

    # 0. right(최대값) 찾기
    right = 0
    for i in range(N):
        tmp = perfos[i] * foods[i]
        if tmp > right:
            right = tmp

    # 1. 이분탐색
    left = 0
    current_max_score = float("inf")
    while left <= right:
        mid = (left + right) // 2

        # 1-1. 이 mid에 맞추기 위해 훈련해야 하는 k값 찾기
        k_current = 0
        for i in range(N):
            if perfos[i] * foods[i] > mid:
                j = 1
                while j <= perfos[i]:
                    if foods[i] * (perfos[i] - j) <= mid:
                        k_current += j
                        break
                    j += 1

        if k_current > K:
            left = mid + 1
        else:
            if mid < current_max_score:
                current_max_score = mid
            right = mid - 1

    print(f'#{tc} {current_max_score}')