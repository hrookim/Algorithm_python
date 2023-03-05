# 토마토가 모두 익을 때까지의 최소 날짜/ 저장될 때부터 모든 토마토가 익어있는 상태이면 0/ 토마토가 모두 익지는 못하는 상황이면 -1
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    global farm, to_visit
    last_day = 0  # 익는데 걸리는 최소 시간
    
    while to_visit:
        cn, cm, today = to_visit.popleft()
        farm[cn][cm] = 1
        last_day = today
        
        for dn, dm in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nn, nm = cn+dn, cm+dm
            if 0 <= nn < N and 0 <= nm < M and not farm[nn][nm]:
                to_visit.append((nn, nm, today+1))
    
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
cnt_zero = 0
for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            to_visit.append((i, j, 0))
        if not farm[i][j]:
            cnt_zero += 1

# 저장될 때부터 익어있는 상황
if cnt_zero == 0:
    print(0)
# 그 외의 상황
else:
    ans = []
    ans.append(bfs())
    print(max(ans))
    
    
