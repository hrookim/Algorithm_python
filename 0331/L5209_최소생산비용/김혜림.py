# N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산
# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산

import sys
sys.stdin = open('input.txt')


def find_min_cost(ci, visit_j, ssum):
    global arr, answer
    # 0. 백트랙킹
    if ssum >= answer:
        return
    
    # 1. 종료조건
    if not visit_j:
        answer += ssum
        if ssum < answer:
            answer = ssum
            return
    
    # 2. 이동하기
    for j in range(len(visit_j)):
        # 내가 선택하는 것은 여기서 결정이 된다!
        find_min_cost(ci+1, visit_j[:j] + visit_j[j+1:], ssum+arr[ci][visit_j[j]])
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    answer = 100 * N
    visit = list(range(N))
    find_min_cost(0, visit, 0)
    print(f'#{tc} {answer}')