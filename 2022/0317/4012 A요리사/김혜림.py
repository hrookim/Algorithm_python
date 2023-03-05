import sys, itertools
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    synergies = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 식재료 선정하기
    A_foods = list(itertools.combinations(range(N), N//2))
    B_foods = []
    foods = set(range(N))
    for A_food in A_foods:
        B_foods.append(tuple(foods - set(A_food))) 
    
    # 2. 두개씩 묶어서 시너지 계산 -> 맛 알아내기
    min_diff = 10000000000
    for n in range(len(A_foods)):
        A_cooks = list(itertools.combinations(A_foods[n], 2))
        B_cooks = list(itertools.combinations(B_foods[n], 2))
        A_synergy = B_synergy = 0
        for A_cook in A_cooks:
            A_synergy += synergies[A_cook[0]][A_cook[1]] + synergies[A_cook[1]][A_cook[0]]
        for B_cook in B_cooks:
            B_synergy += synergies[B_cook[0]][B_cook[1]] + synergies[B_cook[1]][B_cook[0]]
        
        # 2-1. 맛의 차이가 가장 적은 경우 찾기
        taste = abs(A_synergy - B_synergy)
        if taste < min_diff:
            min_diff = taste
        
    print(f'#{tc} {min_diff}')    
            
    