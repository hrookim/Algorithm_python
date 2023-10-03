"""
문제를 잘 보면 N개의 막대기만 만들면 되는 것이고, 만들다가 남거나 안쓰이는 막대는 버려도 상관이 없다!!!
그러므로 전체 길이를 mid 길이의 몫으로 더하는 것은 옳지 않다.
"""

import sys
sys.stdin = open("input1.txt")

K, N = map(int, input().split())

lens = []
for _ in range(K):
    n = int(input())
    lens.append(n)

lens.sort(reverse=True)
max_len = lens[0]
max_N_len = 0
left, right = 1, max_len

while left <= right:
    mid = (left + right) // 2
    
    tmp = 0
    for len in lens:
        tmp += len//mid
    
    if tmp >= N:
        if mid > max_N_len:
            max_N_len = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_N_len)
    