import sys
from collections import deque
sys.stdin = open('input2.txt')


def bfs(i, j):
    to_visit = deque([[i, j, 0]])
    visited[i][j][0] = 1
    while to_visit:
        ci, cj, crushed = to_visit.popleft()

        for di, dj in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if (ni, nj) == (N - 1, M - 1):
                    return visited[ci][cj][crushed] + 1
                # 벽 부수고 이동하기 (무조건 처음 만난 벽 하나를 부수게 되어있다.)
                if matrix[ni][nj] and not crushed:
                    to_visit.append([ni, nj, crushed + 1])
                    visited[ni][nj][crushed + 1] = visited[ci][cj][crushed] + 1
                # 벽 안 부수고 이동하기 (그냥 원래 하던대로)
                if matrix[ni][nj] == 0 and visited[ni][nj][crushed] == 0:
                    to_visit.append([ni, nj, crushed])
                    visited[ni][nj][crushed] = visited[ci][cj][crushed] + 1
    else:
        return -1


N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
# 벽을 안 부쉈다면 왼쪽 좌표에 저장, 부쉈다면 오른쪽 좌표에 저장
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
answer = bfs(0, 0)
print(answer)