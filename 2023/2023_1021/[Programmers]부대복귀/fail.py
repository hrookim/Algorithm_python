from collections import deque


def solution(n, roads, sources, destination):
    answer = []

    def BFS(s, destination):
        nonlocal n, graph

        q = deque([(s, 0)])
        visited = [0] * (n + 1)
        visited[s] = 1

        while q:
            ci, cmove = q.popleft()

            if ci == destination:
                return cmove

            for ni in graph[ci]:
                if not visited[ni]:
                    visited[ni] = 1
                    q.append((ni, cmove + 1))


        else:
            return -1

    graph = [[] for _ in range(n + 1)]

    for road in roads:
        a, b = road[0], road[1]

        graph[a].append(b)
        graph[b].append(a)

    for s in sources:
        a = BFS(s, destination)
        answer.append(a)

    return answer