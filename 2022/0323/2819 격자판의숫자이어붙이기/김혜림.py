# 6번 이동 -> 7자리 수 만들기
# 중복 괜찮음 / 서로 다른 일곱자리 수 개수 반환
import sys
sys.stdin = open('input.txt')


def dfs(i, j, nums):
    global memo
    # 0. zerobase: 자릿수 == 7일 때,
    if len(nums) == 7:
        memo.add(''.join(nums))
        return
    
    # 1. 이동가능한 범위에서 dfs
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= i + di < 4 and 0 <= j + dj < 4:
            dfs(ni, nj, nums + [matrix[ni][nj]])


T = int(input())

for tc in range(1, T + 1):
    matrix = [list(input().split()) for _ in range(4)]

    memo = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, [matrix[i][j]])

    print(f'#{tc} {len(memo)}')