# 이용권의 가격과, 이용 계획을 받아서 최소금액으로 이용할 계획을 짠다.
import sys
sys.stdin = open('input.txt')


def plan_min_cost():
    global prices
    min_prices = [0]*13
    
    for m in range(1, 13):
        # 일간 vs 한달
        min_prices[m] = min(prices[0] * annual_plans[m], prices[1]) + min_prices[m-1]
        
        if m >= 3:
            min_prices[m] = min(min_prices[m], prices[2] + min_prices[m-3])
            
    return min_prices[-1] if min_prices[-1] < prices[-1] else prices[-1]
    
        
T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    annual_plans = [0] + list(map(int, input().split()))
    
    print(f'#{tc} {plan_min_cost()}')
    
    