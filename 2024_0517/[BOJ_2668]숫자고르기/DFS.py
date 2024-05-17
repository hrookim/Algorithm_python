import sys
sys.stdin = open("input1.txt")

sys.setrecursionlimit(10**6)


def dfs(idx, start):
    visited[idx] = 1

    nidx = matrix[idx]

    if not visited[nidx]:
        dfs(nidx, start)
    elif visited[nidx] and nidx == start:
        result.append(nidx)


N = int(input())
matrix = [0] + [int(input()) for _ in range(N)]

result = []
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    dfs(i, i)

print(len(result))
for res in sorted(result):
    print(res)