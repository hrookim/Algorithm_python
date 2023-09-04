from collections import deque

# 격자크기, 팀 개수, 라운드 수
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

person = (1, 2, 3)
not_person = (0, 4)
group_dict = dict()


def move():
    global group_dict, N, graph

    for ky, group in group_dict.items():
        hi, hj = group["head"]
        ti, tj = group["tail"]

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nhi, nhj = hi + di, hj + dj
            nti, ntj = ti + di, tj + dj
            if 0 <= nhi < N and 0 <= nhj < N and graph[nhi][nhj] == 4:
                graph[nhi][nhj] = 1
                graph[hi][hj] = 2
                group_dict[ky]["head"] = (nhi, nhj)

            if 0 <= nti < N and 0 <= ntj < N and graph[nti][ntj] == 2:
                graph[nti][ntj] = 3
                graph[ti][tj] = 4
                group_dict[ky]["tail"] = (nti, ntj)


def throw(graph, k):
    global score, N

    def find_head(i, j):
        visited = [[0] * N for _ in range(N)]
        q = deque([(i, j, 1)])

        while q:
            ci, cj, cturn = q.popleft()

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    if graph[ni][nj] == 2:
                        q.append((ni, nj, cturn + 1))
                        visited[ni][nj] = 1
                    elif graph[ni][nj] == 1:
                        return cturn + 1, ni, nj

    idx = k // N % 4

    if idx == 0:
        """i는 나머지로 고정, j 가변"""
        i = k % N
        for j in range(N):
            if graph[i][j] == 1:
                score += 1
                for group in group_dict.values():
                    if group["head"] == (i, j):
                        group["head"], group["tail"] = group["tail"], group["head"]
                break
            elif graph[i][j] in (2, 3):
                s, hi, hj = find_head(i, j)
                score += s ** 2
                for group in group_dict.values():
                    if group["head"] == (hi, hj):
                        group["head"], group["tail"] = group["tail"], group["head"]
                break


    elif idx == 1:
        """j는 나머지 고정, i는 역순"""
        j = k % N
        for i in reversed(range(N)):
            if graph[i][j] == 1:
                score += 1
                for group in group_dict.values():
                    if group["head"] == (i, j):
                        group["head"], group["tail"] = group["tail"], group["head"]
                        break
            elif graph[i][j] in (2, 3):
                s, hi, hj = find_head(i, j)
                score += s ** 2
                for group in group_dict.values():
                    if group["head"] == (hi, hj):
                        group["head"], group["tail"] = group["tail"], group["head"]
                break

    elif idx == 2:
        """j range 역순, i 나머지 역"""
        i = N - 1 - k % N
        for j in reversed(range(N)):
            if graph[i][j] == 1:
                score += 1
                for group in group_dict.values():
                    if group["head"] == (i, j):
                        group["head"], group["tail"] = group["tail"], group["head"]
                        break
            elif graph[i][j] in (2, 3):
                s, hi, hj = find_head(i, j)
                score += s ** 2
                for group in group_dict.values():
                    if group["head"] == (hi, hj):
                        group["head"], group["tail"] = group["tail"], group["head"]
                        break
    elif idx == 3:
        """i는 전체 j는 나머지 역 고정"""
        j = N - 1 - k % N
        for i in range(N):
            if graph[i][j] == 1:
                score += 1
                for group in group_dict.values():
                    if group["head"] == (i, j):
                        group["head"], group["tail"] = group["tail"], group["head"]
                        break
            elif graph[i][j] in (2, 3):
                s, hi, hj = find_head(i, j)
                score += s ** 2
                for group in group_dict.values():
                    if group["head"] == (hi, hj):
                        group["head"], group["tail"] = group["tail"], group["head"]
                break


# 0. group_dict 정보를 만드는 과정
m = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            m += 1
            total = 1

            stack = [(i, j)]
            visited = [[0] * N for _ in range(N)]
            visited[i][j] = 1
            while stack:
                ci, cj = stack.pop()

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                        if graph[ni][nj] == 2:
                            visited[ni][nj] = 1
                            total += 1
                            stack.append((ni, nj))
                        elif graph[ni][nj] == 3:
                            visited[ni][nj] = 1
                            total += 1
                            group_dict[m] = {
                                "head": (i, j),
                                "tail": (ni, nj),
                            }
            else:
                group_dict[m]["total"] = total

score = 0
for k in range(K):
    move()
    throw(graph, k)
print(score)