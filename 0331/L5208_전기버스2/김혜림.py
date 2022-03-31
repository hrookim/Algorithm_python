# 정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 
# 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다. 마지막 정류장에는 배터리가 없당
import sys
sys.stdin = open('input.txt')


def go_by_bus(ci, cnt, remain):
    global N, lst, min_charge
    # 0. 백트랙킹
    if cnt >= min_charge:
        return
    
    # 1. 종료조건
    if ci >= N:
        if cnt < min_charge:
            min_charge = cnt
        return
    
    # 2-1. 충전 후 
    cnt += 1
    remain = lst[ci]
    # 2-2. 조건에 맞게 이동하기
    for i in range(remain, 0, -1):
        if remain - i >= 0:
            go_by_bus(ci+i, cnt, remain-i)
    
    
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    
    min_charge = 101
    go_by_bus(1, -1, 0)
    
    print(f'#{tc} {min_charge}')
    