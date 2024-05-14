import sys
sys.stdin = open("input.txt")

from collections import deque

# M, N, K그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한
# 나머지 부분이 몇 개의 분리된 영역으로 나뉘는지,
# 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 출력하는 프로그램 


def BFS(i, j):
    global matrix, area, visited
    q = deque([[i, j]])

    c_area = 1
    visited[i][j] = 1
    
    while q:
        ci, cj = q.popleft()
        
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= nj < N and 0 <= ni < M and not visited[ni][nj] and not matrix[ni][nj]:
                visited[ni][nj] = 1
                q.append([ni, nj])
                c_area += 1
    
    else:
        area.append(c_area)

M, N, K = map(int, input().split())     # 모두 100이하

rectangles = []
for _ in range(K):
    # 왼쪽 아래가 0, 0 / 오른쪽 위 N(가로), M(세로)
    # 왼쪽 아래 꼭짓점 + 오른쪽 위 꼭짓점
    point = list(map(int, input().split()))
    rectangles.append(point)


matrix = [[0]*N for _ in range(M)]

for lj, li, rj, ri in rectangles:
    for i in range(li, ri):
        for j in range(lj, rj):
            matrix[i][j] = 1

visited = [[0] * N for _ in range(M)]
cnt = 0
area = []
for i in range(M):
    for j in range(N):
        if not matrix[i][j] and not visited[i][j]:
            cnt += 1
            BFS(i, j)
            

print(cnt)
area.sort()
print(*area)
