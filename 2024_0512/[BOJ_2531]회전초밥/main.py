import sys 
sys.stdin = open('input2.txt') 

input = sys.stdin.readline

# 손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구하는 프로그램

# 회전초밥 벨트 위 접시 수 N, 초밥 가짓수 d, 연속해서 먹는 접시 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().split())

# 슬라이딩 윈도우??????
sushi_belt = []
for _ in range(N):
    sushi_belt.append(int(input()))
    

# window 초기값 설정
subset = sushi_belt[0:k] + [c]
subset_info = dict()
for s in subset:
    if not subset_info.get(s):
        subset_info[s] = 1
    else:
        subset_info[s] += 1

max_sushi = len(subset_info)

for n in range(1, N):
    if subset_info[sushi_belt[n-1]] == 1:
        subset_info.pop(sushi_belt[n-1])   
    elif subset_info[sushi_belt[n-1]] > 1:
        subset_info[sushi_belt[n-1]] -= 1
    
    if n + k > N:
        current_sushi = sushi_belt[n+k-N-1]
    else:
        current_sushi = sushi_belt[n+k-1]
        
    if not subset_info.get(current_sushi):
        subset_info[current_sushi] = 1
    else:
        subset_info[current_sushi] += 1
    
    if len(subset_info) > max_sushi:
        max_sushi = len(subset_info)

print(max_sushi)
        
    
    
