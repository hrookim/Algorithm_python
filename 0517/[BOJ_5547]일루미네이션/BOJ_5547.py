import sys 
from collections import deque

sys.stdin = open('input3.txt') 

W, H = map(int, input().split())

arr = [[0] * (W+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(H)] + [[0] * (W+2)]


def get_line(i, j):
    global total, W, H
    cur = arr[i][j]
    # 홀수 i라면
    if i % 2:
        if arr[i-1][j] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i-1][j+1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i][j-1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i][j+1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i+1][j+1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i+1][j] != cur:
            total = total + 1 if cur == 1 else total - 1

    # 짝수 i라면
    else:
        if arr[i-1][j-1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i-1][j] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i][j-1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i][j+1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i+1][j-1] != cur:
            total = total + 1 if cur == 1 else total - 1
        if arr[i+1][j] != cur:
            total = total + 1 if cur == 1 else total - 1


def is_alone_bfs(i, j):
    global arr
    visited = [(i, j)]
    to_visit = deque([(i, j)])
    arr[i][j] = 9
    while to_visit:
        ci, cj = to_visit.popleft()
        if ci % 2:
            for di, dj in [(-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0)]:
                ni, nj = ci+di, cj+dj
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 9
                    if ni in (1, H) or nj in (1, W):
                        return False
                    if (ni, nj) not in visited:
                        to_visit.append((ni, nj))
                        visited.append((ni, nj))
                        
        else:
            for di, dj in [(-1, -1), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 0)]:
                ni, nj = ci+di, cj+dj
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 9
                    if ni in (1, H) or nj in (1, W):
                        return False
                    if (ni, nj) not in visited:
                        to_visit.append((ni, nj))
                        visited.append((ni, nj))

    return visited        

        
total = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        # 연결된 요소를 파악해서 6면에서 연결된 면만큼 빼기
        if arr[i][j] == 1:
            get_line(i, j)
        # 주위 6면이 다 건물로 둘러싸여있다면 
        elif arr[i][j] == 0:
            if i in (1, H) or j in (1, W):
                continue
            minus_list = is_alone_bfs(i, j)
            if minus_list:
                for mi, mj in minus_list:
                    get_line(mi, mj)
   
print(total)