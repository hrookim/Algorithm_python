# 격자크기, 박멸 년수, 제초제 확산 범위, 제초제 잔여 년수
N, M, K, C = map(int, input().split())

# 각칸의 나무수, 빈칸 0, 벽 -1
graph = [list(map(int, input().split())) for _ in range(N)]


def grow():
    global N, graph, current_tree

    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                current_tree[i][j] = 1

                # 1-1. 인접한 나무 수 찾기
                cnt = 0
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] > 0:
                        cnt += 1

                # 1-2. 인접한 나무 수 만큼 성장하기
                graph[i][j] += cnt


def reproduce():
    global N, graph, current_tree, current_herbicide

    for i in range(N):
        for j in range(N):
            if current_tree[i][j]:
                cnt = 0
                tmp = []
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and not current_tree[ni][nj] and graph[ni][nj] >= 0 and not \
                    current_herbicide[ni][nj]:
                        cnt += 1
                        tmp.append((ni, nj))

                if cnt > 0:
                    trees = graph[i][j] // cnt
                    for ni, nj in tmp:
                        graph[ni][nj] += trees


def eliminate():
    global N, K, C, graph, current_herbicide, result

    maxi, maxj, maxtree = 0, 0, 0
    for i in range(N):
        for j in range(N):
            # 3-1. 제초될 나무 찾기
            if graph[i][j] >= 0:  # 현재 나무라면
                elim_tree = graph[i][j]
                for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                    k = 1
                    while k <= K:
                        ni, nj = i + di * k, j + dj * k
                        if 0 <= ni < N and 0 <= nj < N:
                            if graph[ni][nj] > 0:  # 나무인 경우는                
                                elim_tree += graph[ni][nj]
                            else:
                                break
                        k += 1

                if elim_tree > maxtree:
                    maxi, maxj = i, j
                    maxtree = elim_tree

            # 3-2. 현재 제초제 영향 있는 곳 년수 줄이기
            if current_herbicide[i][j] > 0:
                current_herbicide[i][j] -= 1

    # 3-3. 제초하기
    result += graph[maxi][maxj]
    graph[maxi][maxj] = 0
    current_herbicide[maxi][maxj] = C
    for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
        k = 1
        while k <= K:
            ni, nj = maxi + di * k, maxj + dj * k
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] > 0:  # 나무인 경우는                
                    result += graph[ni][nj]
                    graph[ni][nj] = 0
                    current_herbicide[ni][nj] = C
                elif graph[ni][nj] == 0:  # 벽이나 나무가 0인 칸 만나면 더 이상 퍼지지 않음
                    current_herbicide[ni][nj] = C
                    break
                else:
                    break
            k += 1


current_herbicide = [[0] * N for _ in range(N)]
result = 0

for _ in range(M):
    current_tree = [[0] * N for _ in range(N)]
    grow()
    reproduce()
    eliminate()

print(result)