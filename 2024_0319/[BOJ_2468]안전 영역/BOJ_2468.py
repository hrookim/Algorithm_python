import sys 
from collections import deque
sys.stdin = open('input2.txt') 


def DFS(i, j, visited):
    global N
    stack = deque([(i, j)])
    
    while stack:    
        ci, cj = stack.pop()
        
        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                stack.append((ni, nj))
    

N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]

# 1. 강수량 범위 구하기
max_rain = 0
min_rain = 101
for i in range(N):
    for j in range(N):
        if land[i][j] > max_rain:
            max_rain = land[i][j]
        if land[i][j] < min_rain:
            min_rain = land[i][j]
            
# 2. 강수량 돌면서 최대 안전영역 찾기
max_safety = 1
for current_rain in range(min_rain, max_rain):
    # 2-1. 잠긴지역 표시
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if land[i][j] <= current_rain:
                visited[i][j] = 1

    # 2-2. 안 잠긴지역 개수 세기
    current_safety = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                current_safety += 1
                visited[i][j] = 1
                DFS(i, j, visited)
                
    # 2-3. 최대 안전영역 갱신하기
    if current_safety > max_safety:
        max_safety = current_safety
        
print(max_safety)