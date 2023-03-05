# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# N개의 자연수 중에서 M개를 고른 수열
#   같은 수를 여러 번 골라도 된다.
#   고른 수열은 비내림차순이어야 한다.
#   길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

import sys 
from itertools import combinations_with_replacement
sys.stdin = open('input2.txt') 

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

all_subset = sorted(map(sorted, set(combinations_with_replacement(numbers, M))))
i = 0
while i < len(all_subset):
    if i == len(all_subset) - 1:
        print(*all_subset[i])
        i += 1
    elif all_subset[i] == all_subset[i+1]:
        all_subset = all_subset[:i] + all_subset[i+1:]
    else:
        print(*all_subset[i])
        i += 1