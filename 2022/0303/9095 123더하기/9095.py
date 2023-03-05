import sys
sys.stdin = open('input.txt')


def dp(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        memo = [0, 1, 2, 4]
        for i in range(4, N+1):
            memo.append(memo[i-1] + memo[i-2] + memo[i-3])
        return memo[-1]
    
    
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp(N))
    
    
