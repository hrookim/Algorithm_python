import sys
sys.stdin = open('input2.txt')


def find_min_coin(coins, K):
    cnt = 0
    
    for coin in coins[::-1]:
        if coin <= K:
            cnt += K//coin
            K %= coin
            if K == 0:
                return cnt
            
            
N, K = map(int, input().split())

coins = []
for _ in range(N):
    c = int(input())
    if c <= K:
        coins.append(c)

print(find_min_coin(coins, K))

