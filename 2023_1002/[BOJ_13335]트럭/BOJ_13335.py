from collections import deque
import sys 
sys.stdin = open('input3.txt') 

# 트럭개수, 다리너비, 최대하중
N, W, L = map(int, input().split())

trucks = deque(list(map(int, input().split())))

time = 0
bridge = [0] * W
while len(trucks) > 0 or sum(bridge) > 0:
    time += 1
    # 0. 요소 한칸씩 앞으로 보내기 
    bridge = bridge[1:] + [0]    
    
    # 1. 다리에 여유 있고 남는 트럭도 있다면, 트럭 하나 보내기    
    if len(trucks) > 0 and sum(bridge) < L:
        t = trucks.popleft()
        if sum(bridge) + t <= L :
            bridge[-1] = t
        else:
            trucks.appendleft(t)

print(time)
