import sys
sys.stdin = open("input.txt")


def find_routes(i, j, route):
    global curr_routes, N
    
    # 0. route에 추가하기 위한 작업
    if len(route) == 4:
        curr_routes.append(route)
        return
    
    # 1. 그렇지 않다면 route를 찾으러 가야 함
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            visited[ni][nj] = 1
            find_routes(ni, nj, route + [(ni, nj)])
            visited[ni][nj] = 0
        

def make_combinations(curr, tree_current, product):
    global N, M, max_product, mans_routes
    # 0. 재귀 깊이 도달했으면, 최대 값인지 확인
    if curr == M:
        if product > max_product:
            max_product = product
        return
    
    # 1. 그게 아니라면 파고들기
    for rt in mans_routes[curr]:
        ctree = [tree_current[n][:] for n in range(N)]
        cproduct = product
        for i, j in rt:
            if ctree[i][j]:
                cproduct += ctree[i][j]
                ctree[i][j] = 0

        make_combinations(curr+1, [ctree[n][:] for n in range(N)], cproduct)
        
        
# ======INPUT======
N, M = map(int, input().split())
tree_array = [list(map(int, input().split())) for _ in range(N)]
mans_location = [tuple(map(int, input().split())) for _ in range(M)]


# A. 친구가 이동할 수 있는 모든 경로 구하기
mans_routes = []
for mi, mj in mans_location:
    curr_routes = []
    visited = [[0] * N for _ in range(N)]
    visited[mi-1][mj-1] = 1                           # 문제에서의 좌표 설정은 1씩 크다
    find_routes(mi-1, mj-1, [(mi-1, mj-1)])     # 문제에서의 좌표 설정은 1씩 크다
    
    mans_routes.append(curr_routes)


# B. 모든 경로에 대한 조합을 찾아서 최대값 찾기 => 36*36*36
max_product = 0
for m in range(M):
    make_combinations(0, tree_array, 0)

print(max_product)