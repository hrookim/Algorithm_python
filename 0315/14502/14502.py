import sys
from itertools import combinations
sys.stdin = open('input2.txt')


def bfs():
    while to_visit:
        (ci, cj) = to_visit.pop(0)
        visited[ci][cj] = 2

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
                if not visited[ni][nj]:
                    to_visit.append((ni, nj))


def find_zero():
    result = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m] == 2:
                result += 1
            if matrix[n][m] == 1:
                result += 1
    return N * M - result


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 0. 빈칸, 바이러스 위치 찾기
nulls = []
viruses = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            nulls.append((i, j))
        elif matrix[i][j] == 2:
            viruses.append((i, j))
            
# 1. combination 써서 벽 세우기
temp_walls = list(combinations(nulls, 3))
zeros = []

for temp_wall in temp_walls:
    visited = [[0] * M for _ in range(N)]
    to_visit = []
    to_visit += viruses
    for wall in temp_wall:
        matrix[wall[0]][wall[1]] = 1
    # BFS 이동 후 0인 영역 구하기
    bfs()
    zeros.append(find_zero())
    for wall in temp_wall:
        matrix[wall[0]][wall[1]] = 0

print(max(zeros))

