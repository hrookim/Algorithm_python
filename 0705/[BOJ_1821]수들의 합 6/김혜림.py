# 이전에 일반항을 잘못 생각해서 새로 짠 코드

import sys 
from itertools import permutations
sys.stdin = open('input1.txt') 

N, F = map(int, input().split())


pascal = []
numbers = list(range(1, N+1))

A = Q = 1
for r in range(N):
    if r == 0 or r == N-1:
        pascal.append(1)
    else:
        A *= (N-r)
        Q *= r
        pascal.append(int(A/Q))

perms = permutations(numbers)
for p in perms:
    tmp = 0
    for i in range(N):
        tmp += p[i]*pascal[i]
    if tmp == F:
        print(*p)
        break
        
        
    
