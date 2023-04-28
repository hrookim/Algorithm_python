from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    point_dict = dict()

    for i in range(N):
        for j in range(M):
            if maps[i][j] == "S":
                point_dict["S"] = [i, j]
            elif maps[i][j] == "L":
                point_dict["L"] = [i, j]
            elif maps[i][j] == "E":
                point_dict["E"] = [i, j]

    def BFS(start, i, j):
        to_visit = deque([[i, j, 0]])
        ei, ej = point_dict["E"][0], point_dict["E"][1]
        si, sj = point_dict["S"][0], point_dict["S"][1]

        s_least_time = float("inf")
        e_least_time = float("inf")
        visited = [[0] * M for _ in range(N)]
        while to_visit:
            ci, cj, ctime = to_visit.popleft()
            visited[ci][cj] = 1

            if ci == ei and cj == ej and ctime < e_least_time:
                e_least_time = ctime
            elif ci == si and cj == sj and ctime < s_least_time:
                s_least_time = ctime

            if s_least_time != float("inf") and e_least_time != float("inf"):
                return s_least_time + e_least_time

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < M:
                    if maps[ni][nj] != "X" and not visited[ni][nj]:
                        to_visit.append([ni, nj, ctime + 1])
        else:
            return -1

    answer = BFS("L", point_dict["L"][0], point_dict["L"][1])
    return answer