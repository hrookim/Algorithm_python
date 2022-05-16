"""
도시 안에 2개의 매장을 지으려고 한다. 도시는 N 개의 건물과 M 개의 도로
i 번째 도로는 서로 다른 두 건물 Ai 번과 Bi 번 사이를 1 시간에 양방향으로 이동할 수 있는 도로이다.
2개의 건물을 골라서 치킨집을 열려고 한다.
모든 건물에서의 접근성의 합을 최소화
건물 X 의 접근성은 X 에서 가장 가까운 호석이 두마리 치킨집까지 왕복하는 최단 시간이다

최적의 위치가 될 수 있는 건물 2개의 번호와 그 때의 "모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단 시간의 총합"을 출력하자. 
만약 이러한 건물 조합이 여러 개라면, 건물 번호 중 작은 게 더 작을수록, 작은 번호가 같다면 큰 번호가 더 작을수록 좋은 건물 조합이다.
"""

import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input1.txt') 
input = sys.stdin.readline


def BFS(s, candi):
    global N, graph, current_distance, min_distance
    
    visited = [0] * (N+1)
    to_visit = deque([(s, 0)])
    
    while to_visit:
        # 가지치기
        if current_distance > min_distance:
            return True

        c, dist = to_visit.popleft()
        visited[c] = 1
        
             
        for f in graph[c]:
            if f in candi:
                dist += 1
                current_distance += dist
                return
            if not visited[f]:
                to_visit.append((f, dist+1))
                visited[f] = 1
                

N, M = map(int, input().split())    # 건물, 도로

# 0. 그래프 생성하기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1. 치킨집 후보
total_bd = list(range(1, N+1))
candidates = list(combinations(total_bd, 2))

# 2. 완전탐색: 치킨집 후보들이 정해졌을 때, 그 치킨집까지의 최소거리 
min_distance = float('inf')
min_candi = []
for candi in candidates:
    rest = list(set(total_bd) - set(candi))

    # 2-1. 각 건물에서 치킨집까지의 최소거리의 합을 구하고
    current_distance = 0    
    for s in rest:
        isexceed = BFS(s, candi)
        if isexceed:
            break
    
    # 2-2. 최솟값을 갱신
    if current_distance < min_distance:
        min_distance = current_distance
        min_candi = [*candi]

print(*min_candi, min_distance*2)
