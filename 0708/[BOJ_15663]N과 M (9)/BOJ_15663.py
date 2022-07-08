import sys 
from itertools import permutations
sys.stdin = open('input2.txt') 

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

all_subset = sorted(set(permutations(numbers, M)))
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