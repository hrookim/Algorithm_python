# 1은 참가자가 들어갈 수 있는 칸, 0은 들어갈수 없는 칸
# 4**5 = 1024, 5! = 120 
# bfs 하기!

import sys
from collections import deque
from itertools import product, permutations
sys.stdin = open('input7.txt') 

f1 = [list(map(int, input().split())) for _ in range(5)]
f2 = [list(map(int, input().split())) for _ in range(5)]
f3 = [list(map(int, input().split())) for _ in range(5)]
f4 = [list(map(int, input().split())) for _ in range(5)]
f5 = [list(map(int, input().split())) for _ in range(5)]


def bfs():
    global cube
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    to_visit = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    
    while to_visit:
        cz, ci, cj = to_visit.popleft()
        c_move = visited[cz][ci][cj]
        
        # 종료조건
        if (cz, ci, cj) == (4, 4, 4):
            return c_move - 1
        
        # 이동
        for dz, di, dj in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nz, ni, nj = cz+dz, ci+di, cj+dj
            if 0 <= nz < 5 and 0 <= ni < 5 and 0 <= nj < 5 and cube[nz][ni][nj] and not visited[nz][ni][nj]:
                to_visit.append((nz, ni, nj))
                visited[nz][ni][nj] = c_move+1
        

def turn_floor(arr, n):
    ans = [[0]*5 for _ in range(5)]
    if n == 0:
        return arr
    
    cnt = 0
    while cnt < n:
        for j in range(5):
            for i in range(4, -1, -1):
                ans[j][4-i] = arr[i][j]
        arr = [ans[x][:] for x in range(5)]
        cnt += 1
    return ans
        

answer = 200
for seq in product(range(4), range(4), range(4), range(4), range(4)):
    tf1 = turn_floor(f1, seq[0])
    tf2 = turn_floor(f2, seq[1])
    tf3 = turn_floor(f3, seq[2])
    tf4 = turn_floor(f4, seq[3])
    tf5 = turn_floor(f5, seq[4])
    
    for seqq in permutations(range(5), 5):
        cube = []
        for q in seqq:
            if q == 0:
                cube.append(tf1)
            elif q == 1:
                cube.append(tf2)
            elif q == 2:
                cube.append(tf3)
            elif q == 3:
                cube.append(tf4)
            elif q == 4:
                cube.append(tf5)
    
        # (0, 0, 0)이 1이여야 bfs 가능
        if cube[0][0][0]:
            tmp = bfs()
            if tmp and tmp < answer:
                answer = tmp
if answer >= 200:
    answer = -1
        
print(answer)
    