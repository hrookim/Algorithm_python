"""
N2개의 방이 N×N형태의 방
위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 출발해야 가장 많은 개수의 방을 이동할 수 있는지?
"""
import sys
sys.stdin = open('input.txt')


def go(i, j):  # bfs 이동해보기?
    global cnt
    to_visit = [(i, j)]
    
    while to_visit:
        # 현재 위치 current i j
        ci, cj = to_visit.pop(0)
        visited[ci][cj] = 1
        cnt += 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if matrix[ni][nj] == matrix[ci][cj] + 1:
                    to_visit.append((ni, nj))
 
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 시작지점을 달리해서 한칸씩 이동할 수 있으면 이동해보기
    result, idx = 0, 1000000000000
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            cnt = 0
            go(i, j)
            tmp = matrix[i][j]
            if cnt > result:
                result = cnt
                idx = tmp
            elif cnt == result and tmp < idx:
                result = cnt
                idx = tmp
    
    print(f'#{tc} {idx} {result}')