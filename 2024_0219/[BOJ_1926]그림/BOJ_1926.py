import sys 
from collections import deque
sys.stdin = open('input1.txt') 


def BFS(i, j):
    global maxPicture, array, visited
    
    to_visit = deque([(i, j)])
    areaPicture = 0
    visited[i][j] = 1
    
    while to_visit:
        ci, cj = to_visit.popleft()
        areaPicture += 1
        
        for di, dj in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and array[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                to_visit.append((ni, nj))
    
    if areaPicture > maxPicture:
        maxPicture = areaPicture
        

N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

maxPicture = 0
numPicture = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if array[i][j] and not visited[i][j]:
            numPicture += 1
            
            BFS(i, j)
        
print(numPicture)        
print(maxPicture)