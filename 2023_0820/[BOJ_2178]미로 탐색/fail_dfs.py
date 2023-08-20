import sys 
sys.stdin = open('input3.txt') 


def DFS(i, j, move):
    global ei, ej, result, maze, visited
    
    # 0. 종료조건
    if i == ei and j == ej:
        result = min(move, result)
        return
    
    # 1. 갈 수 있는 곳에 한해서 이동하기
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = move+1
            DFS(ni, nj, move+1)
        elif ni == ei and nj == ej:
            DFS(ni, nj, move+1)

N, M = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]

si, sj = 0, 0
ei, ej = N-1, M-1

visited = [[0]*M for _ in range(N)]
visited[si][sj] = 1
result = float("inf")

DFS(si, sj, 1)
print(result)

