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

    def BFS(start, end, i, j):
        to_visit = deque([[i, j, 0]])
        ei, ej = point_dict[end][0], point_dict[end][1]

        least_time = float("inf")
        visited = [[0] * M for _ in range(N)]
        while to_visit:
            ci, cj, ctime = to_visit.popleft()
            visited[ci][cj] = 1

            if ci == ei and cj == ej:
                least_time = min(ctime, least_time)
                return least_time

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < M:
                    if maps[ni][nj] != "X" and not visited[ni][nj]:
                        to_visit.append([ni, nj, ctime + 1])

        return least_time

    start_to_lever = BFS("S", "L", point_dict["S"][0], point_dict["S"][1])
    if start_to_lever == -1:
        return -1
    lever_to_end = BFS("E", "L", point_dict["E"][0], point_dict["E"][1])
    if lever_to_end == -1:
        return

    answer = start_to_lever + lever_to_end
    return answer


maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))