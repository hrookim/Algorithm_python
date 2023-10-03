import sys
from collections import deque
sys.stdin = open("input.txt")
# input = sys.stdin.readline


# di, dj로 나타낸 신호등
positions = {
    0: (0, 1),  # 우
    1: (-1, 0), # 상
    2: (0, -1), # 좌
    3: (1, 0)   # 하
}
traffic_light = [
    [(-1, 0, 1), (0, 1, 0), (1, 0, 3)],
    [(0, -1, 2), (-1, 0, 1), (0, 1, 0)],
    [(1, 0, 3), (0, -1, 2), (-1, 0, 1)],
    [(0, -1, 2), (1, 0, 3), (0, 1, 0)],
    [(-1, 0, 1), (0, 1, 0)],
    [(0, -1, 2), (-1, 0, 1)],
    [(1, 0, 3), (0, -1, 2)],
    [(1, 0, 3), (0, 1, 0)],
    [(0, 1, 0), (1, 0, 3)],
    [(-1, 0, 1), (0, 1, 0)],
    [(0, -1, 2), (-1, 0, 1)],
    [(0, -1, 2), (1, 0, 3)],
]


def DFS(start):
    global road_matrix, traffic_light, T, visited

    to_visit = deque([start])
    while to_visit:
        ci, cj, c_time, position = to_visit.pop()

        if c_time <= T:
            visited[ci][cj] = 1
            tl = road_matrix[ci][cj][c_time % 4]
            if (tl - 1) % 4 == position:
                for di, dj, p in traffic_light[tl - 1]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        to_visit.append((ni, nj, c_time + 1, p))


N, T = map(int, input().split())

road_matrix = [[[] for _ in range(N)] for _ in range(N)]

for n in range(N ** 2):
    i, j = n // N, n % N
    light = list(map(int, input().split()))
    road_matrix[i][j] += light
visited = [[0 for _ in range(N)] for _ in range(N)]

DFS((0, 0, 0, 1))

result = 0
for a in range(N):
    result += sum(visited[a])

print(result)