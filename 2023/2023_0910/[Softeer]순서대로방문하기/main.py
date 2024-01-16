import sys
sys.stdin = open("input2.txt")

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

spots = []
for _ in range(M):
    a, b = map(int, input().split())
    spots.append((a - 1, b - 1))


def find(i, j, idx):
    """
    :param i: 현재 행 위치 
    :param j: 현재 열 위치
    :param idx: 목표로할 spots의 index
    :return: 
    """
    global result, spots, visited
    # 0. 종료 조건
    if idx == M-1 and spots[-1][0] == i and spots[-1][1] == j:
        result += 1
        return
    
    # 1. 도착해야 할 지점이라면 그 다음을 향해 가기
    if spots[idx][0] == i and spots[idx][1] == j:
        find(i, j, idx+1)
        
    # 2. 이동하기
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and not graph[ni][nj]:
            visited[ni][nj] = 1
            find(ni, nj, idx)
            visited[ni][nj] = 0


result = 0
visited = [[0] * N for _ in range(N)]
si, sj = spots[0][0], spots[0][1]
visited[si][sj] = 1
find(si, sj, 1)
print(result)