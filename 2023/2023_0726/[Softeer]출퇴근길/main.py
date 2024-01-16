import sys

sys.setrecursionlimit(10 ** 9)


def DFS(v, graph, visited):
    if visited[v] == 1:  # 이미 방문을 했을 경우
        return

    # 방문 하지 않았을 경우
    else:
        visited[v] += 1
        for nv in graph[v]:
            DFS(nv, graph, visited)


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
graph_rev = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph_rev[y].append(x)
S, T = map(int, input().split())

fromS = [0] * (N + 1)
fromS[T] = 1
DFS(S, graph, fromS)

toT = [0] * (N + 1)
DFS(T, graph_rev, toT)

fromT = [0] * (N + 1)
fromT[S] = 1
DFS(T, graph, fromT)

toS = [0] * (N + 1)
DFS(S, graph_rev, toS)

result = 0
for n in range(1, N + 1):
    if fromT[n] and fromS[n] and toS[n] and toT[n]:
        result += 1

print(result - 2)