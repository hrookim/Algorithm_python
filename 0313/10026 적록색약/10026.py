import sys
sys.stdin = open("input.txt")


def dfs_delta(i, j):
    to_visit = [(i, j)]
    while to_visit:
        ci, cj = to_visit.pop()  # current i j 
        if not visited[ci][cj]:
            visited[ci][cj] = True
            color = matrix[ci][cj]
            
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni = ci + di
                nj = cj + dj
                if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == color:
                    if not visited[ni][nj]:
                        to_visit.append((ni, nj))
    
    
def find_area_normal():
    area = 0
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'R':
                matrix[i][j] = 1
            elif matrix[i][j] == 'G':
                matrix[i][j] = 2
            else:
                matrix[i][j] = 3
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                area += 1
                dfs_delta(i, j)
    return area


def find_area_blindness():
    area = 0
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                matrix[i][j] = 1
            
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                area += 1
                dfs_delta(i, j)
    return area


N = int(input())

matrix = [list(input()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
print(find_area_normal(), end=" ")
visited = [[False]*N for _ in range(N)]
print(find_area_blindness())
