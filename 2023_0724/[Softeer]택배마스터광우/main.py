import sys
input = sys.stdin.readline
from itertools import permutations


def find_min_weight(rail):
    global N, M, K, min_result
    result = 0

    i, c = 0, 0
    while i < K:

        if result > min_result:
            return float("inf")

        curr_pocket = 0
        while curr_pocket < M:
            curr_pocket += rail[c%N]
            c += 1
        else:
            i += 1
            if curr_pocket == M:
                result += curr_pocket
            else:
                c -= 1
                result += curr_pocket - rail[c%N]
    return result


# 레일 개수, 택배 바구니 무게, 일의 시행 횟수
N, M, K = map(int, input().split())

rails_weight = list(map(int, input().split()))

min_result = float("inf")
for current_rail in permutations(rails_weight, N):
    min_result = min(min_result, find_min_weight(current_rail))
print(min_result)