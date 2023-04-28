from collections import deque


def solution(maps):
    def BFS(i, j):
        to_visit = deque([[i, j, 0]])

        s_least_time = float("inf")
        e_least_time = float("inf")
        visited = [[0] * M for _ in range(N)]
        visited[i][j] = 1
        while to_visit:
            ci, cj, ctime = to_visit.popleft()

            if maps[ci][cj] == "E" and ctime < e_least_time:
                e_least_time = ctime
            elif maps[ci][cj] == "S" and ctime < s_least_time:
                s_least_time = ctime

            if s_least_time != float("inf") and e_least_time != float("inf"):
                return s_least_time + e_least_time

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < M:
                    if maps[ni][nj] != "X" and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        to_visit.append([ni, nj, ctime + 1])
        else:
            return -1

    N = len(maps)
    M = len(maps[0])

    for i in range(N):
        for j in range(M):
            if maps[i][j] == "L":
                answer = BFS(i, j)
                return answer

