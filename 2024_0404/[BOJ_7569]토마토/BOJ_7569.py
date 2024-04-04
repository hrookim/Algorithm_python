import sys 
sys.stdin = open('input3.txt') 

from collections import deque


def BFS(to_visit):
    global boxes, N, M, H
    
    result = 0
    while to_visit:
        ch, ci, cj, cmove = to_visit.popleft()
        result = max(result, cmove)
        
        for dh, di, dj in [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]:
            nh, ni, nj = ch+dh, ci+di, cj+dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and boxes[nh][ni][nj] == 0:
                boxes[nh][ni][nj] = 1
                to_visit.append((nh, ni,nj, cmove+1))
                
    else:
        return result


def is_all_ripen():
    global boxes, H, N, M
    
    result = False
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[h][i][j] == 0:
                    return False
                elif boxes[h][i][j] == 1:
                    result = True

    return result


M, N, H = map(int, input().split())

boxes = []
for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    boxes.append(box)
    
if is_all_ripen():
    print(0)
else:
    q = deque([])

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[h][i][j] == 1:
                    q.append((h, i, j, 0))
    
    result = BFS(q)
    
    if is_all_ripen():
        print(result)
    else:
        print(-1)