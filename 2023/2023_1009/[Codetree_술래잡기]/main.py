import sys
from collections import deque

sys.stdin = open("input4.txt")


def people_move():
    global M, people, chaser, di, dj
    result = [[0]*N for _ in range(N)]
    m = 0
    while m < len(people):
        m += 1
        i, j, d = people.popleft()
        
        # 0. 술래랑 거리 3이내인 경우
        if abs(i-chaser[0]) + abs(j-chaser[1]) <= 3:
            
            # 1. 이동할 위치롤 보고
            ni, nj = i+di[d], j+dj[d]
            if ni < 0 or ni >= N:
                d = (d+2) % 4
                ni = i+di[d]
            elif nj < 0 or nj >= N:
                d = (d+2) % 4
                nj = j+dj[d]
            
            # 2-1. 술래가 거기 없다면 이동을 한다.
            if (ni, nj) != chaser:
                result[ni][nj] += 1
                people.append((ni, nj, d))
            # 2-2. 술래가 있었다면 그냥 원래대로 들어간다.
            else:
                result[i][j] += 1
                people.append((i, j, d))
        
        else:
            result[i][j] += 1
            people.append((i, j, d))
    return result    
    

def chaser_move(k):
    global people, chaser, chaser_track, di, dj, score, people_map
    i, j, d = chaser_track.popleft()
    chaser = (i, j)
    for p in range(3):
        ni, nj = i+di[d]*p, j+dj[d]*p
        if 0 <= ni < N and 0 <= nj < N and not tree_map[ni][nj] and people_map[ni][nj]:
            score += k * people_map[ni][nj]
            
            cnt = 0
            while cnt < len(people):
                ii, jj, dd = people.popleft()
                if ii == ni and jj == nj:
                    continue
                else:
                    people.append((ii, jj, dd))
                cnt += 1
                

N, M, H, K = map(int, input().split())

# 도망자 초기 배치
people = deque([])
people_map = [[0]*N for _ in range(N)]
for _ in range(M):
    x, y, d = map(int, input().split())
    people.append((x-1, y-1, d))
    people_map[x-1][y-1] = 1

# 나무 초기 배치
tree_map = [[0]*N for _ in range(N)]
for _ in range(H):
    x, y = map(int, input().split())
    tree_map[x-1][y-1] = 1

# 술래 초기 배치 + 달팽이로 이동할 곳 찾기    
chaser = (N//2, N//2)
chaser_track = deque([[N//2, N//2, 0]])
chaser_map = [[0]*N for _ in range(N)]
chaser_map[N//2][N//2] = 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for _ in range(N**2 - 1):
    i, j, d = chaser_track[-1]
    
    ni, nj = i+di[d], j+dj[d]
    if not chaser_map[ni][nj]:
        chaser_map[ni][nj] = 1
        
        nd = (d + 1) % 4
        nni, nnj = ni+di[nd], nj+dj[nd]
        if not chaser_map[nni][nnj]:
            chaser_track.append([ni, nj, nd])
        else:
            chaser_track.append([ni, nj, d])


chaser_map = [[0]*N for _ in range(N)]
chaser_map[0][0] = 1
chaser_track[-1][2] = 2
for _ in range(N ** 2 - 1):
    i, j, d = chaser_track[-1]

    ni, nj = i + di[d], j + dj[d]
    if not chaser_map[ni][nj]:
        chaser_map[ni][nj] = 1
        
        nni, nnj = ni + di[d], nj + dj[d]
        if 0 <= nni < N and 0 <= nnj < N and not chaser_map[nni][nnj]:
            chaser_track.append([ni, nj, d])
        else:
            nd = (d-1 +4) % 4
            chaser_track.append([ni, nj, nd])

chaser_track.pop()
k = K
while k - 2*(N**2-1) > 0:
    chaser_track += chaser_track 
    k -= 2*(N**2-1)

score = 0
chaser_track.popleft()
for k in range(1, K+1):
    people_map = people_move()
    chaser_move(k)
    
    if len(people) == 0:
        break
    
print(score)