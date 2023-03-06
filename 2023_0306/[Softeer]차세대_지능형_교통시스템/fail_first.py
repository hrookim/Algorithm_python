import sys
from collections import deque
input = sys.stdin.readline
# di, dj로 나타낸 신호등
traffic_light = [
    [(-1, 0), (0, 1), (1, 0)], [(0, -1), (-1, 0), (0, 1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (1, 0), (0, 1)],
    [(-1, 0), (0, 1)], [(0, -1), (-1, 0)], [(1, 0), (0, -1)], [(1, 0), (0, 1)],
    [(0, 1), (1, 0)], [(-1, 0), (0, 1)], [(0, -1), (-1, 0)], [(0, -1), (1, 0)],
]


def DFS(start):
    global road_matrix, traffic_light, T, visited
    result = 0

    to_visit = deque([start])
    while to_visit:
        ci, cj, c_time, pi, pj = to_visit.pop()

        if not visited[ci][cj] and c_time <= T:
            visited[ci][cj] = 1
            result += 1
            tl = road_matrix[ci][cj][c_time % 4]
            for di, dj in traffic_light[tl-1]:
                ni, nj = ci+di, cj+dj
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    to_visit.append((ni, nj, c_time+1, ci, cj))
    return result


N, T = map(int, input().split())

road_matrix = [[[] for _ in range(N)] for _ in range(N)] 

for n in range(N**2):
    i, j = n % N, n // N
    light = list(map(int, input().split()))
    road_matrix[i][j] += light

visited = [[0 for _ in range(N)] for _ in range(N)]

print(DFS((0, 0, 0, 1, 0)))