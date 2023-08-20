from collections import deque
import sys 
sys.stdin = open('input4.txt') 

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
q = deque([(0, 0, 1)])

while q:
    i, j, move = q.popleft()
    visited[i][j] = move
    
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = move+1
            q.append((ni, nj, move+1))


print(visited[N-1][M-1])