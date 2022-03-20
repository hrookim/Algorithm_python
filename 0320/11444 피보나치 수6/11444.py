# 피보나치 수
# 0번째 - 0, 1번째 - 1
import sys
from collections import deque
sys.stdin = open('input.txt')


def fibo(N):
    fn = deque([0, 1])
    
    if N <= 1:
        return fn[N]
    else:
        for _ in range(2, N+1):
            fn.append(fn[0] + fn[1])
            fn.popleft()
        return fn[1]
    
    
N = int(input())
ans = fibo(N) % 1000000007
print(ans)
# 시간초과...ㅠㅜ
