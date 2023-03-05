import sys

sys.stdin = open('input.txt')

directions = {
    1: [(0, 1), (1, 0), (0, -1), (-1, 0)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}


def is_connected(ni, nj, ci, cj):
    tmp = []
    key = matrix[ni][nj]

    for di, dj in directions[key]:
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

    to_visit = [[] for _ in range(L + 2)]
    to_visit[1].append((R, C))
    for time in range(1, L + 1):
        if time == L:
            cnt += len(set(to_visit[time]))
            return
        to_visit[time] = list(set(to_visit[time]))
        while to_visit[time]:
            # 현재 위치 current i j
            ci, cj = to_visit[time].pop()
            visited[ci][cj] = 1
            cnt += 1
            key = matrix[ci][cj]

            for di, dj in directions[key]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj]:
                    if not visited[ni][nj] and is_connected(ni, nj, ci, cj):
                        to_visit[time + 1].append((ni, nj))


T = int(input())

for tc in range(1, T + 1):
    # N M은 매트릭스, R C는 뚜껑위치, L은 소요시간
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    bfs(R, C)
    print(f'#{tc} {cnt}')