import sys
sys.stdin = open("input2.txt")


from collections import deque
F, S, G, U, D = map(int, input().split())


def BFS(S, G, U, D):
    visited = dict()
    
    visited[S] = 1
    to_visit = deque([(S, 0)])
    
    while to_visit:
        cstair, cmove = to_visit.popleft()
        
        # 위로 이동
        nstair = cstair + U
        if 1 <= nstair <= F and not visited.get(nstair):
            nmove = cmove + 1
            
            if nstair == G:
                print(nmove)
                return
            visited[nstair] = 1
            to_visit.append((nstair, nmove))

        nstair = cstair - D
        if 1 <= nstair <= F and not visited.get(nstair):
            nmove = cmove + 1

            if nstair == G:
                print(nmove)
                return
            visited[nstair] = 1
            to_visit.append((nstair, nmove))

    else:
        print("use the stairs")

if S == G:
    print(0)
else:
    BFS(S, G, U, D)