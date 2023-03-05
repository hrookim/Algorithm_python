# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(N, cnt):
    global M
    # 네개의 연산을 처리한 값을 넣어주는데, 이미 나왔던 적이 있는 값이라면 안 추가해도 된다.
    operated = set()
    operated.add(N)
    to_operate = deque([(N, cnt)])
    
    while to_operate:
        cn, ccnt = to_operate.popleft()
        if cn == M:
            return ccnt
        
        if cn+1 not in operated and cn+1 <= 1000000:
            to_operate.append([cn + 1, ccnt + 1])
            operated.add(cn+1)
        if cn-1 not in operated and 1 <= cn-1 <= 1000000:
            to_operate.append([cn-1, ccnt + 1])
            operated.add(cn-1)
        if cn*2 not in operated and cn-1 <= 1000000:
            to_operate.append([cn*2, ccnt + 1])
            operated.add(cn*2)
        if cn-10 not in operated and 1 <= cn-10 <= 1000000:
            to_operate.append([cn-10, ccnt+1])
            operated.add(cn-10)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs(N, 0)
    print(f'#{tc} {ans}')
        
    