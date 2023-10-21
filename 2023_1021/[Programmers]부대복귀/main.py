from collections import deque


def solution(n, roads, sources, destination):
    answer = []

    def BFS(destination):
        nonlocal graph, min_move

        q = deque([(destination, 0)])
        min_move[destination] = 0
        while q:
            ci, cmove = q.popleft()

            for ni in graph[ci]:
                if min_move[ni] == -1:
                    min_move[ni] = cmove + 1
                    q.append((ni, cmove + 1))

    graph = [[] for _ in range(n + 1)]

    for road in roads:
        a, b = road[0], road[1]

        graph[a].append(b)
        graph[b].append(a)

    min_move = [-1] * (n + 1)
    BFS(destination)

    for s in sources:
        answer.append(min_move[s])

    return answer