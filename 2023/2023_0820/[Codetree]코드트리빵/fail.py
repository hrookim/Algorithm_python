from collections import deque

N, M = map(int, input().split())  # 격자크기, 사람 수
array = [list(map(int, list(input().split()))) for _ in range(N)]

# 편의점 위치 저장
stores = dict()
for i in range(1, M + 1):
    ii, jj = map(int, input().split())
    stores[i] = [ii - 1, jj - 1]

# 베이스캠프 위치 저장    
basecamps = []
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            basecamps.append((i, j))

# 사람 위치 판별
people = dict()
for i in range(1, M + 1):
    people[i] = []


def find_bc(store_i, store_j):
    """
    :param store_i: 그 사람이 갈 편의점의 i좌표 
    :param store_j: 그 사람이 갈 편의점의 j좌표
    :return: 최단거리 베이스캠프의 i, j
    """
    route = 2 * N + 1
    i, j = 0, 0

    for bc_i, bc_j in basecamps:
        if not visited[bc_i][bc_j]:
            tmp = abs(store_i - bc_i) + abs(store_j - bc_j)
            if tmp < route:
                route = tmp
                i, j = bc_i, bc_j
            elif tmp == route:
                if bc_i < i:
                    i, j = bc_i, bc_j
                elif i == bc_i and bc_j < j:
                    j = bc_j
    return i, j


def BFS(current, store):
    """
    최단거리 경로를 찾는 함수
    :return: 최단거리 루트 배열
    """
    q_visited = [[0] * N for _ in range(N)]
    q = deque([[*current, [current]]])  # 시작점 위치와 경로
    while q:
        ci, cj, route = q.popleft()
        q_visited[ci][cj] = 1

        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and not q_visited[ni][nj]:
                if [ni, nj] == store:
                    return deque(route + [[ni, nj]])
                q_visited[ni][nj] = 1
                q.append([ni, nj, route + [[ni, nj]]])


visited = [[0] * N for _ in range(N)]
total_visited = 0
people_visited = [0] * (M + 1)
people_routes = dict()  # 최단거리를 담는 딕셔너리

time = 0
while total_visited < M:
    time += 1

    # 1. 아직 모두 격자에 들어오지 않았을 때
    if time <= M:
        for k, v in people.items():
            if not people_visited[k] and v:
                ci, cj = people_routes[k].popleft()
                people[k] = [ci, cj]
                if people[k] == stores[k]:
                    visited[ci][cj] = 1
                    total_visited += 1
                    people_visited[k] = 1
                    for kk, vv in people.items():
                        if not people_visited[kk] and k != kk and vv:
                            people_routes[kk] = BFS(vv, stores[kk])
                            people_routes[kk].popleft()

            if time == k:
                bc_i, bc_j = find_bc(stores[k][0], stores[k][1])
                visited[bc_i][bc_j] = 1
                people[k] = [bc_i, bc_j]
                people_routes[k] = BFS([bc_i, bc_j], stores[k])
                people_routes[k].popleft()


    # 2. 격자에 모두 들어오고 난 이후에는..
    else:
        for k, v in people.items():
            if not people_visited[k]:
                ci, cj = people_routes[k].popleft()
                people[k] = [ci, cj]
                if people[k] == stores[k]:
                    visited[ci][cj] = 1
                    total_visited += 1
                    people_visited[k] = 1
                    for kk, vv in people.items():
                        if not people_visited[kk] and k != kk and vv:
                            people_routes[kk] = BFS(vv, stores[kk])
                            people_routes[kk].popleft()


else:
    print(time)