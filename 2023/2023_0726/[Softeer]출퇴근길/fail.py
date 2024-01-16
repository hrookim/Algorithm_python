import sys
from collections import deque

input = sys.stdin.readline


def DFS(start, end):
    result = set()

    to_visit = deque([(start, [start])])
    while to_visit:
        if len(result) == N:
            return result

        cs, croute = to_visit.pop()

        if cs == end:
            result |= set(croute)
            # print(croute)
            continue

        for v in graph[cs]:
            if len(croute) >= 3 and v == croute[-2]:
                continue
            nroute = croute + [v]
            to_visit.append((v, nroute))
    return result


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
S, T = map(int, input().split())

house_routes = DFS(S, T)
office_routes = DFS(T, S)

print(len(house_routes & office_routes) - 2)
