import sys 
sys.stdin = open('input2.txt') 

input = sys.stdin.readline

# 정점의 개수, 간선의 개수, 시작 정점
N, M, V = map(int, input().split())
# 정점의 번호는 1~N까지, 방문할 수 있는 정점이 여러개인 경우 작은 것을 먼저 방문



# 1. DFS 함수
def DFS(start):
    result = []
    visited = [False for _ in range(N+1)]
    
    to_visit = [start]
    while to_visit:
        current = to_visit.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            to_visit += sorted(graph[current], reverse=True)
    else:
        print(*result)

# 2. BFS 함수
def BFS(start):
    result = []
    visited = [False for _ in range(N+1)]
    
    to_visit = [start]
    while to_visit:
        current = to_visit.pop(0)
        if not visited[current]:
            visited[current] = True
            result.append(current)
            to_visit += sorted(graph[current])
    else:
        print(*result)

# 0. 그래프 제작
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
DFS(V)
BFS(V)