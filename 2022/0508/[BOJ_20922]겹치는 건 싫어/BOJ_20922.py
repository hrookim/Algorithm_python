import sys 
sys.stdin = open('input2.txt') 

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

e = max_seq = tmp_seq = 0
check = {}
for s in range(N):
    while True:
        current = numbers[e]
        # 1. 방문기록 남기기 
        if check.get(current):
            # 1-1. 종료조건!
            if check.get(current) == K:
                break
            check[current] += 1
        else:
            check[current] = 1
        
        tmp_seq += 1
        if e < N-1:
            e += 1
        elif e == N-1:
            break
        
    
    # 2. 최장수열 갱신
    if tmp_seq > max_seq:
        max_seq = tmp_seq
    
    # 3. 하나 빼주기
    tmp_seq -= 1
    check[numbers[s]] -= 1
    
print(max_seq)