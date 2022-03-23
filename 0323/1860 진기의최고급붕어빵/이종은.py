import sys
sys.stdin = open('input.txt')

def sell_K_bread():
    time = 0
    K_bread = 0

    # 진기는 가장 늦게 오는 손님의 시간만큼 영업한다.
    while time < max(coming_customers):
        time += 1

        # M 초에 도달할때마다 붕어빵은 K개만큼 누적된다.
        if time % M == 0:
            K_bread += K

        # 때마침 도착한 손님이 있다면
        if time in coming_customers:

            # 붕어빵을 팔 수 있다.
            K_bread -= 1

            # 그랬더니 붕어빵이 음수면..? IMPOSSIBLE
            if K_bread < 0:
                    return f'#{tc} Impossible'

    # while문이 중간에 return 안됐으면 진기는 붕어빵을 성공적으로 팔았다!
    return f'#{tc} Possible'


T = int(input())
for tc in range(1, T + 1):

    # 예약손님 몇명? (N)명 / M 초마다 붕어빵 K 개 만들 수 있다.
    N, M, K = map(int, input().split())
    coming_customers = list(map(int, input().split()))
    coming_customers.sort()

    # 오픈하자마자 오는 손님이 있다면 IMPOSSBILE !!
    if 0 in coming_customers:
        print(f'#{tc} Impossible')
    else:
        print(sell_K_bread())