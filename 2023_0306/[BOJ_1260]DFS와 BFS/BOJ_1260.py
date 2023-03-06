import sys 
from collections import deque
sys.stdin = open('input2.txt') 


#. DFS
def DFS(graph, start):
    global visited
    to_visit = deque([start])
    result = []
    
    while to_visit:
        current = to_visit.pop()
        if not visited[current]:
            visited[current] = 1
            result.append(current)
            to_visit += sorted(graph[current], reverse=True)
        
    return result

#. BFS
def BFS(graph, start):
    global visited
    to_visit = deque([start])
    result = []
    
    while to_visit:
        current = to_visit.popleft()
        if not visited[current]:
            visited[current] = 1
            result.append(current)
            to_visit += sorted(graph[current])
    return result
    

#. 정점의 개수, 간선의 개수, 시작점
N, M, S = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    l, r = map(int, input().split())
    graph[l].append(r)
    graph[r].append(l)

visited = [0 for _ in range(N+1)]
print(*DFS(graph, S))
visited = [0 for _ in range(N+1)]
print(*BFS(graph, S))
