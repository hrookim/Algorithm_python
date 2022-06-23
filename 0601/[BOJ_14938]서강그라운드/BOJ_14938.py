"""
각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다. 
예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 
예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.
"""

import sys 
sys.stdin = open('input1.txt') 


def DFS(start, remain_l):
    global tmp, visited, items, graph
    # 0. 종료지점
    if remain_l <= 0:
        tmp += items[start]
        return
    
    # 1. 이동해서 아이템획득하기
    tmp += items[start]
    for next_point in graph[start]:
        if next_point[1] <= remain_l and not visited[next_point[0]]:
            visited[next_point[0]] = 1
            DFS(next_point[0], remain_l-next_point[1])


# 지역 N, 수색범위 M, 길의개수 R
N, M, R = map(int, input().split())

items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
# [0, 5, 7, 8, 2, 3] 
# [[], [(4, 5), (2, 3)], [(5, 4), (3, 3), (1, 3)], [(2, 3)], [(1, 5)], [(2, 4)]]
INF = float('inf')

distances = [INF for _ in range(N+1)]

answer = 0
for n in range(1, N+1):
    tmp = 0
    visited = [0 for _ in range(N + 1)]
    visited[n] = 1
    DFS(n, R)
    if tmp > answer:
        answer = tmp

print(answer)