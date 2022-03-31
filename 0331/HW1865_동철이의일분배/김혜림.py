# N명 N개의 일 -> 공평하게 하나씩 분배. 성공률 적혀있음
# 주어진 일이 모두 성공할 확률의 Max값 구하기
import sys
sys.stdin = open('input.txt')


def find_max_prob(ci, visit_j, prob):
    global arr, ans
    # 0. 백트랙킹
    if prob < ans:
        return

    # 1. 종료조건
    if not visit_j:
        if prob > ans:
            ans = prob
            return
        
    # 2. 방문하기 / ci행에서의 선택은 여기서 이뤄진다.
    for j in range(len(visit_j)):
        if arr[ci][visit_j[j]] == 0: 
            continue
        find_max_prob(ci+1, visit_j[:j]+visit_j[j+1:], prob*arr[ci][visit_j[j]]/100)
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    visit = list(range(N))
    find_max_prob(0, visit, 1)
    
    print(f'#{tc} {ans*100:.6f}')