# 예약제로 손님 받음. N명 -> M초 -> K개 붕어빵
# 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 웨이팅없이 붕어빵 제공할 수 있는가?
import sys
sys.stdin = open('input1.txt')


def is_possible(people):
    global N, M, K
    fish = 0    # 특정 시간동안 만들어진 붕어빵 수
    # 1. 손님이 처음 오는 시간이 붕어빵 만들어지기 전이면 "불가능"
    if min(people) < M:
        return 'Impossible'
    
    # 2. 마지막 손님이 오는 시간대까지 붕어빵 제작
    last_p = max(people)
    for time in range(1, last_p + 1):
        # 2-1. M의 배수인 시간이 되면 K마리가 완성되므로,
        if time % M == 0:
            fish += K
        
        # 2-2. 이때 오는 손님이 있다면, 붕어빵 판매
        for p in people:
            if time == p:
                fish -= 1
                # 2-3. 판매 후 붕어빵 음수되면 "불가능"
                if fish < 0:
                    return 'Impossible'
    
    # 3. 다 만들어서 마지막 손님까지 팔았는데, 붕어빵 음수아니면 "가능"
    if fish >= 0:
        return 'Possible'
    
    
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    
    print(f'#{tc} {is_possible(people)}')
    