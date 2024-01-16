from collections import deque
import sys 
sys.stdin = open('input1.txt') 

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def BFS(i, j):
    global arr
    visited = [[0]*M for _ in range(N)]
    
    q = deque([(i, j, 0)])
    visited[i][j] = 1
    while q:
        ci, cj, cl = q.popleft()
        
        if arr[ci][cj]:
            return cl    
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1 
                q.append((ni, nj, cl+1))
                


result_list = [[0]*M for _ in range(N)]

max_l = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            l = BFS(i, j)
            result_list[i][j] = l
            if l > max_l:
                max_l = l


print(max_l)    
            