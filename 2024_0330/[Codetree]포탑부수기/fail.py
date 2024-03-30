import sys
sys.stdin = open("input11.txt")


# 1. 공격자 선정하기
def select_lowest(k):
    global current_tower, attack_log, relevant_log, N, M
    
    low_value = 10000
    low_list = []
    for i in range(N):
     for j in range(M):
         if 0 < current_tower[i][j] <= low_value:
             low_value = current_tower[i][j]
             low_list.append((-low_value, attack_log[i][j], i+j, j, i))
    low_list.sort(reverse=True)

    li, lj = (low_list[0][4], low_list[0][3])
    current_tower[li][lj] += N+M
    attack_log[li][lj] = k
    relevant_log[li][lj] = 1
    return (li, lj)
 
# 2. 공격대상 선정하기 
def select_highest():
    global current_tower, relevant_log, attacker
    
    high_value = 0
    high_list = []
    for i in range(N):
        for j in range(M):
            if current_tower[i][j] > 0 and (i, j) != attacker: # 공격자를 제외하기 위함
                if current_tower[i][j] >= high_value:
                    high_value = current_tower[i][j]
                    high_list.append((-high_value, attack_log[i][j], i+j, j, i))
    
    if high_list:
        high_list.sort()
        hi, hj = high_list[0][4], high_list[0][3]
        relevant_log[hi][hj] = 1        
        return (hi, hj)
    else:
        return False


from collections import deque
def find_routes2():
    global current_tower, attacker, defender, N, M, moves, routes

    to_visit = deque([(*attacker, [], 0)])
    while to_visit:
        ci, cj, curr_routes, curr_moves = to_visit.popleft()
        if curr_moves >= moves:
            continue
            
        if (ci, cj) == defender:
            if curr_moves < moves:
                moves = curr_moves
                routes = curr_routes
            continue

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = (ci + di) % N, (cj + dj) % M
            if 0 <= ni < N and 0 <= nj < M and current_tower[ni][nj] > 0 and (ni, nj) not in curr_routes:
                to_visit.append((ni, nj, curr_routes + [(ni, nj)], curr_moves+1))


# 3. 레이저 공격하기
def laser_attack(defender, routes):
    global current_tower, relevant_log, attack_power
    
    half_power = attack_power // 2
    for (i, j) in routes:
        if (i, j) == defender:
            if current_tower[i][j] - attack_power < 0:
                current_tower[i][j] = 0
            else:
                current_tower[i][j] -= attack_power
        else: 
            if current_tower[i][j] - half_power < 0:
                current_tower[i][j] = 0
            else:
                current_tower[i][j] -= half_power
        relevant_log[i][j] = 1


def bomb_attack():
    global current_tower, attacker, defender, attack_power, relevant_log, N, M

    ci, cj = defender
    if current_tower[ci][cj] - attack_power < 0:
        current_tower[ci][cj] = 0
    else:
        current_tower[ci][cj] -= attack_power

    half_power = attack_power // 2
    for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        ni, nj = (ci+di)%N, (cj+dj)%M
        if (ni, nj) != attacker:    # 공격자는 이 공격에 영향을 받지 않는다.
            if 0 <= ni < N and 0 <= nj < M and current_tower[ni][nj] > 0:
                if current_tower[ni][nj] - half_power < 0:
                    current_tower[ni][nj] = 0
                else:
                    current_tower[ni][nj] -= half_power
                relevant_log[ni][nj] = 1
            

def heal():
    global relevant_log
    
    for i in range(N):
        for j in range(M):
            if relevant_log[i][j] == 0 and current_tower[i][j] > 0:
                current_tower[i][j] += 1


N, M, K = map(int, input().split())
current_tower = [list(map(int, input().split())) for _ in range(N)]
attack_log = [[0]*M for _ in range(N)]

for k in range(1, K+1):
    relevant_log = [[0]*M for _ in range(N)]
    attacker = select_lowest(k)      # (i, j)
    attack_power = current_tower[attacker[0]][attacker[1]]
    defender = select_highest()     # (i, j)
    if not defender:    # 부서지지 않은 포탑이 하나가 되면 그 즉시 중단한다
        current_tower[attacker[0]][attacker[1]] -= (N+M)
        break
    routes = []
    moves = 101
    visited = [[0]*M for _ in range(N)]
    find_routes2()
    if routes:
        laser_attack(defender, routes)  
    else:
        bomb_attack()
    heal()
    

# 6. 가장 공격력이 높은 것 출력
max_power = 0
for n in range(N):
    for m in range(M):
        if current_tower[n][m] > max_power:
            max_power = current_tower[n][m]

print(max_power)