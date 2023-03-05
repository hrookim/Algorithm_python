import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    global farm, to_visit
    last_day = 0  # 익는데 걸리는 최소 시간

    while to_visit:
        cn, cm, last_day = to_visit.popleft()

        for dn, dm in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nn, nm = cn + dn, cm + dm
            if 0 <= nn < N and 0 <= nm < M and farm[nn][nm] == 0:
                farm[nn][nm] = 1  # 백준 질문보고 수정한 부분ㅠㅜ
                to_visit.append((nn, nm, last_day + 1))

    # 토마토가 모두 익지 못한다면
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 0:
                return -1
    # 토마토가 다 익었다면
    return last_day


M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]

to_visit = deque([])
for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            to_visit.append((i, j, 0))

if not to_visit:
    print(-1)
else:    
    print(bfs())
