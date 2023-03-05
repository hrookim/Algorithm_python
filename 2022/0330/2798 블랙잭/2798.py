import sys
input = sys.stdin.readline


def dfs(n, cnt, ssum):
    global M, min_ssum, min_diff, lst
    # 백트랙킹
    if ssum > M:
        return

    # 0. 종료조건
    if cnt >= 3:
        if 0 <= (M - ssum) <= min_diff:
            min_diff = M - ssum
            min_ssum = ssum
        return

    # 1. 선택 OX
    if -1 <= n < N - 1:
        dfs(n + 1, cnt + 1, ssum + lst[n])  # O
        dfs(n + 1, cnt, ssum)  # X


N, M = map(int, input().split())
lst = list(map(int, input().split()))

min_diff = min_ssum = 100000000000
dfs(-1, 0, 0)
print(min_ssum)