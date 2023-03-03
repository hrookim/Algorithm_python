import sys
sys.stdin = open('input.txt') 

input = sys.stdin.readline

T = int(input())

matrix = [
    [0, 4, 3, 3, 4, 3, 2, 2, 1, 2],
    [0, 0, 5, 3, 2, 5, 6, 2, 5, 4],
    [0, 0, 0, 2, 5, 4, 3, 5, 2, 3],
    [0, 0, 0, 0, 3, 2, 3, 3, 2, 1],
    [0, 0, 0, 0, 0, 3, 4, 2, 3, 2],
    [0, 0, 0, 0, 0, 0, 1, 3, 2, 1],
    [0, 0, 0, 0, 0, 0, 0, 4, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
matrix_from_zero = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]

# 0. 교체 횟수 체크
for i in range(10):
    for j in range(10):
        if i > j:
            matrix[i][j] = matrix[j][i]
        else:
            continue

# 1. 변경을 하자
for tc in range(T):
    A, B = map(list, input().split())

    A_cnt, B_cnt = [999] * (5 - len(A)) + A, [999] * (5 - len(B)) + B

    # 변경횟수 합하기
    result = 0
    for idx in range(4, -1, -1):
        if A_cnt[idx] == 999 and B_cnt[idx] == 999:
            continue
        if A_cnt[idx] == 999:
            result += matrix_from_zero[int(B_cnt[idx])]
        elif B_cnt[idx] == 999:
            result += matrix_from_zero[int(A_cnt[idx])]
        else:
            result += matrix[int(A_cnt[idx])][int(B_cnt[idx])]
    print(result)



