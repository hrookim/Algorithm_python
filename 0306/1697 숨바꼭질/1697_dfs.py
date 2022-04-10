import sys
sys.stdin = open("input.txt")


def move(current, time):
    global N, K, min_time
    # 0. 가지치기
    if time >= min_time or current >= 2*K:
        return
    
    # 1. 종료조건
    if current == K:
        if time < min_time:
            min_time = time
        return 
    
    # 2. 이동
    if current <= K//2:
        move(current * 2, time + 1)
    move(current + 1, time + 1)
    move(current - 1, time + 1)


N, K = map(int, input().split())
min_time = float('inf')
if N >= K:
    min_time = N-K
else:
    move(N, 0)
print(min_time)