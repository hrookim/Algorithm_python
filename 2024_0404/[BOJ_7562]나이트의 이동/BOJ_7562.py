import sys 
sys.stdin = open('input1.txt') 

from collections import deque

def BFS(si, sj):
    global N, end_point
    
    to_visit = deque([(si, sj, 0)])
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    while to_visit:
        ci, cj, cmove = to_visit.popleft()
        
        for di, dj in [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]:
            ni, nj = ci+di, cj+dj
            
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                to_visit.append((ni, nj, cmove+1))
                
                if (ni, nj) == end_point:
                    return cmove+1


TC = int(input())

for _ in range(TC):
    N = int(input())
    start_point = tuple(map(int, input().split()))
    end_point = tuple(map(int, input().split()))
    
    if start_point == end_point:
        result = 0
    else:
        result = BFS(*start_point)
    print(result)
    
              