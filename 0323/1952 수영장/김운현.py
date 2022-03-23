import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 이용권 가격들 (1일, 1달, 3달, 1년)
    price = list(map(int, input().split()))
    # 12개월 이용 계획
    plan = list(map(int, input().split()))

    # 각 달까지의 최소비용을 덮어써주는 방식으로 dp 구현
    dp = [0] * 12
    dp[0] = min(price[0] * plan[0], price[1])  # 1월은 직접 계산 (일일권과 한달권 비교)
    dp[1] = dp[0] + min(price[0] * plan[1], price[1])  # 2월
    dp[2] = min(dp[1] + min(price[0] * plan[2], price[1]), price[2])  # 3월 (3달권을 추가로 비교)
    # 4월부터 각각의 경우의 수를 비교하여 최소비용을 넣어줌
    for i in range(3, 12):
        # 3개월권을 이용할 경우와 일일권을 이용할 경우와 한달권을 이용할 경우
        dp[i] = min(dp[i-3] + price[2], dp[i-1] + min(price[0] * plan[i], price[1]))

    # 그 값을 1년권과 비교하여 작은값이 결과
    result = min(dp[11], price[3])

    print(f'#{tc} {result}')