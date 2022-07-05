# 단, 답이 여러 가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.

import sys 
from itertools import combinations
sys.stdin = open('input1.txt') 


N, F = map(int, input().split())

numbers = list(range(1, N+1))
if N == 1 or N == 2:
    print(*numbers)
else:
    ends = list(combinations(numbers, 2))
    for end in ends:
        mids = set(numbers) - set(end)
        
        if sum(end) + (N-1)*sum(mids) == F:
            answer = [end[0]] + sorted(mids) + [end[-1]]
            print(*answer)
            break
            