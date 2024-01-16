import sys
from collections import deque

input = sys.stdin.readline


def DFS(start, end):
    result = set()

    visited = [0] * (N + 1)
    visited[start] += 1
    to_visit = deque([(start, [start], visited[::])])
    while to_visit:
        if len(result) == N:
            return result

        cs, croute, cvisited = to_visit.pop()

        if cs == end:
            result |= set(croute)
            # print(croute, cvisited)
            continue

        for v in graph[cs]:
            if cvisited[v] >= 2:
                continue
            nroute = croute + [v]
            cvisited[v] += 1
            to_visit.append((v, nroute, cvisited[::]))
    return result


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
S, T = map(int, input().split())

house_routes = DFS(S, T)
office_routes = DFS(T, S)
# print(house_routes, office_routes)
print(len(house_routes & office_routes) - 2)
