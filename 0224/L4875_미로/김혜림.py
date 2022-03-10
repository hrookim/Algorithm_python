import sys 
sys.stdin = open('input.txt')


# 재귀 dfs -> delta
def dfs_delta(i, j):
    visited[i][j] = True
    print(to_visit)
    
    # 0. base case
    if matrix[i][j] == 3:
        return True
    # 1. 이동할 수 있는 곳 찾아서 가보기. 상 우 하 좌 순
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        # 2. 갈 수 있는 길이면서
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] != 1:
            # 2. 방문한 적이 없다면 이동
            if not visited[ni][nj]:
                to_visit.append([ni, nj])
                dfs_delta(*to_visit[-1])
                dfs_delta(ni, nj)
            # 2-2. 방문한 적이 있다면 (인데, 없어도 되는 코드여서 당황)
            # else:
            #     to_visit.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    to_visit = [[0, 0]] # 이런 형태로 지나온 길에 대한 좌표를 저장
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                # 시작점 찾아서 출발
                to_visit.append([i, j])
                dfs_delta(i, j)
                break
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 3:
                print(f'#{tc} {int(visited[i][j])}')
