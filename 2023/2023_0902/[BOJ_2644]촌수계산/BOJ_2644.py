import sys 
from collections import deque
sys.stdin = open('input1.txt') 

"""
여러 사람들에 대한 부모 자식 관계가 주어졌을 떄, 주어진 두 사람의 촌수 구하기
"""

N = int(input())                    # 전체 사람수
x, y = map(int, input().split())    # 구할 두 사람의 번호
M = int(input())                    # 부모 관계 개수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

q = deque([(x, 0)])   # 현재 번호와 촌수
visited[x] = 1
result = -1
while q:
    cn, cmove = q.popleft()

    # 0. 도착지점이라면 결과반환
    if cn == y:
        result = cmove
        break
    
    for nn in graph[cn]:
        if not visited[nn]:
            visited[nn] = 1
            q.append((nn, cmove+1))

print(result)