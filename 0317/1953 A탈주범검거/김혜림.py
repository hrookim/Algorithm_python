import sys
sys.stdin = open('input.txt')


def is_connected(ni, nj, ci, cj):
    tmp = []
    # 1: 상하좌우
    if matrix[ni][nj] == 1:
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ti, tj = ni + di, nj + dj
            if 0 <= ti < N and 0 <= tj < M and matrix[ti][tj]:
                tmp.append((ti, tj))
    # 2: 상하
    elif matrix[ni][nj] == 2:
        for di, dj in [(1, 0), (-1, 0)]:
            ti, tj = ni + di, nj + dj
            if 0 <= ti < N and 0 <= tj < M and matrix[ti][tj]:
                tmp.append((ti, tj))
    # 3: 좌우
    elif matrix[ni][nj] == 3:
        for di, dj in [(0, 1), (0, -1)]:
            ti, tj = ni + di, nj + dj
            if 0 <= ti < N and 0 <= tj < M and matrix[ti][tj]:
                tmp.append((ti, tj))
    # 4: 상우
    elif matrix[ni][nj] == 4:
        for di, dj in [(-1, 0), (0, 1)]:
            ti, tj = ni + di, nj + dj
            if 0 <= ti < N and 0 <= tj < M and matrix[ti][tj]:
                tmp.append((ti, tj))
    # 5: 하우
    elif matrix[ni][nj] == 5:
        for di, dj in [(1, 0), (0, 1)]:
            ti, tj = ni + di, nj + dj
            if 0 <= ti < N and 0 <= tj < M and matrix[ti][tj]:
                tmp.append((ti, tj))
    # 6: 하좌
    elif matrix[ni][nj] == 6:
        for di, dj in [(1, 0), (0, -1)]:
            ti, tj = ni + di, nj + dj
            if 0 <= ti < N and 0 <= tj < M and matrix[ti][tj]:
                tmp.append((ti, tj))
    # 7: 상좌
    elif matrix[ni][nj] == 7:
        for di, dj in [(-1, 0), (0, -1)]:
            ti, tj = ni + di, nj + dj
            if 0 <= ti < N and 0 <= tj < M and matrix[ti][tj]:
                tmp.append((ti, tj))
    
    if (ci, cj) in tmp:
        return True
    else:
        False
    

def bfs(R, C):  # bfs 방식으로 간다!
    # 각 번호마다 이동 체크, 연결이 안된 부분은 어떻게 해결??!
    global cnt, L
    
    to_visit = [[] for _ in range(L+2)]
    to_visit[1].append((R, C))
    for time in range(1, L+1):
        if time == L:
            cnt += len(set(to_visit[time]))
            return
        to_visit[time] = list(set(to_visit[time]))
        while to_visit[time]:
            # 현재 위치 current i j
            ci, cj = to_visit[time].pop()
            visited[ci][cj] = 1
            cnt += 1
            
            # 1: 상하좌우
            if matrix[ci][cj] == 1: 
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                        if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                            to_visit[time+1].append((ni, nj))
            # 2: 상하
            elif matrix[ci][cj] == 2:
                for di, dj in [(1, 0), (-1, 0)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                        if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                            to_visit[time+1].append((ni, nj))
            # 3: 좌우
            elif matrix[ci][cj] == 3:
                for di, dj in [(0, 1), (0, -1)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                        if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                            to_visit[time+1].append((ni, nj))
            # 4: 상우
            elif matrix[ci][cj] == 4:
                for di, dj in [(-1, 0), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                        if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                            to_visit[time+1].append((ni, nj))
            # 5: 하우
            elif matrix[ci][cj] == 5:
                for di, dj in [(1, 0), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                        if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                            to_visit[time+1].append((ni, nj))
            # 6: 하좌
            elif matrix[ci][cj] == 6:
                for di, dj in [(1, 0), (0, -1)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                        if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                            to_visit[time+1].append((ni, nj))
            # 7: 상좌
            elif matrix[ci][cj] == 7:
                for di, dj in [(-1, 0), (0, -1)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                        if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                            to_visit[time+1].append((ni, nj))
              
                        
T = int(input())

for tc in range(1, T+1):
    # N M은 매트릭스, R C는 뚜껑위치, L은 소요시간
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    
    bfs(R, C)
    print(f'#{tc} {cnt}')