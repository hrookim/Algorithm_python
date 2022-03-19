# 이동할 때, 벽을 하나는 부수고 이동해도 괜찮다면 그 최단경로는 어떻게 구할까
# (1,1) -> (N,M)
import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(i, j):
    to_visit = deque([[i, j, 1]])
    flag = [0, 0]

    while to_visit:
        ci, cj, move = to_visit.popleft()
        visited[ci][cj] = 1
        for di, dj in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if (ni, nj) == (N-1, M-1):
                    return move + 1
                # 벽인데 부순적 없음
                if flag[0] < 4 and matrix[ni][nj]:
                    # 어떤 공간에서도 부순적이 없다면
                    if flag[1] == 0:
                        to_visit.append([ni, nj, move+1])
                        flag[1] = move
                        flag[0] += 1
                    elif move == flag[1]:
                        to_visit.append([ni, nj, move + 1])
                        flag[0] += 1
                elif not matrix[ni][nj]:
                    to_visit.append([ni, nj, move+1])
    else:
        return -1
 
    
N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = bfs(0, 0)
print(answer)