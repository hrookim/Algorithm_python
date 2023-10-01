import sys
sys.stdin = open("input1.txt")

from queue import PriorityQueue

N = -1
M = -1
P = -1
rabbit_dict = dict()
rabbit_q = PriorityQueue()
loss_score = 0

def prepare(info):
    """
    경주 준비를 하는 함수
    :param info: P부터 시작해서 pid와 d가 P개의 쌍을 이뤄서 들어옴
    """
    global P, rabbit_dict, rabbit_q
    for p in range(P):
        pid, distance = info[2*p], info[2*p+1]
        rabbit_dict[pid] = {
            "score": 0,
            "distance": distance
        }
        
        rabbit_q.put((0, 1+1, 1, 1, pid))
    # print(rabbit_q.queue)

def race(K, S):
    """
    우선순위에 맞게 경주를 진행하는 함수
    :param K: 턴의 횟수
    :param S: 더할 점수
    """
    global rabbit_q, rabbit_dict, loss_score, N, M
    
    moved_rabbit_dict = dict()
    for _ in range(K):
        # 1. 움직일 토끼 뽑기
        total_jump, rc, r, c, pid = rabbit_q.get()
        
        # 2. 움직일 포인트찾기 -> 움직이기
        distance = rabbit_dict[pid]["distance"]
        r_distance = distance % (2*(N-1))
        c_distance = distance % (2*(M-1))
        race_point_q = PriorityQueue()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr*r_distance, c + dc*c_distance
            if 1 <= nr < N+1 and 1 <= nc < M+1:
                race_point_q.put((-nr-nc, -nr, -nc))
            elif not 1 <= nr < N+1:
                cdr = dr
                while True:
                    if 1 <= nr < N+1:
                        break
                    
                    if nr < 1:
                        cdr = -cdr
                        move = -(nr - 1)
                        nr = 1 + cdr*move
                        
                    if nr >= N+1:
                        cdr = -cdr
                        move = nr-N
                        nr = N + cdr*move
                race_point_q.put((-nr-nc, -nr, -nc))

            elif not 1 <= nc < M+1:
                cdc = dc
                while True:
                    if 1 <= nc < M+1:
                        break

                    if nc < 1:
                        cdc = -cdc
                        move = -(nc - 1)
                        nc = 1 + cdc * move

                    if nc >= M + 1:
                        cdc = -cdc
                        move = nc - M
                        nc = M + cdc * move
                race_point_q.put((-nr-nc, -nr, -nc))
                
        _nrc, _nr, _nc = race_point_q.get()
        nnr = -(_nr)
        nnc = -(_nc)
        rabbit_q.put((total_jump+1, nnr+nnc, nnr, nnc, pid))
        moved_rabbit_dict[pid] = (nnr, nnc)
        
        # 3. 다른 토끼들한테 점수주기 ( = 이 토끼한테만 점수 깎기)
        rabbit_dict[pid]["score"] -= (nnr+nnc)
        loss_score += (nnr+nnc)

    # 4. 움직인 토끼 중 가장 우선순위 높은 애한테 점수 주기
    moved_rabbit_q = PriorityQueue()
    for pid, rabbit in moved_rabbit_dict.items():
        r, c = rabbit[0], rabbit[1]
        moved_rabbit_q.put((-r-c, -r, -c, -pid))
    
    _rc, _r, _c, _pid = moved_rabbit_q.get()
    rabbit_dict[-(_pid)]["score"] += S
    

def change_distance(pid, L):
    global rabbit_dict
    rabbit_dict[pid]["distance"] = rabbit_dict[pid]["distance"]*L


def find_the_best():
    global rabbit_dict, loss_score
    max_score = -1
    for pid, rabbit in rabbit_dict.items():
        rabbit["score"] += loss_score
        if rabbit["score"] > max_score:
            max_score = rabbit["score"]
    print(max_score)
    

Q = int(input())
for _ in range(Q):
    commands = list(map(int, input().split()))
    cmd_no = commands[0]
    
    if cmd_no == 100:
        N, M, P = commands[1], commands[2], commands[3]
        prepare(commands[4:])
    elif cmd_no == 200:
        race(commands[1], commands[2])
    elif cmd_no == 300:
        change_distance(commands[1], commands[2])
    elif cmd_no == 400:
        find_the_best()
    
    