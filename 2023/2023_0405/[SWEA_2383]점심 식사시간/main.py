import sys
from itertools import combinations
from collections import deque
sys.stdin = open("sample_input.txt")


def go_for_lunch(subgroup, stair):
    global array
    stair_level = array[stair[0]][stair[1]]
    # 계단까지 도착하는 시간
    people_time_to_stair = []
    for p in subgroup:
        people_time_to_stair.append(abs(p[0]-stair[0]) + abs(p[1]-stair[1]))
    
    people_time_to_stair = deque(sorted(people_time_to_stair))
    people_on_stair = deque()
    
    # 1. 모든 이동시간 계산하기
    time = 0
    while people_time_to_stair:
        time += 1
        
        # 계단 내려가는 이동시간 
        while people_on_stair and people_on_stair[0] == time:
            people_on_stair.popleft()
        
        # 계단까지 가고 있는 이동시간
        while people_time_to_stair[0] < time: 
            if len(people_on_stair) < 3:       
                people_time_to_stair.popleft() 
                
                if not people_time_to_stair:
                    time += stair_level
                    break
                
                people_on_stair.append(time + stair_level)
            else:
                break
    return time


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []
    p = 0
    for i in range(N):
        for j in range(N):
            if array[i][j] == 1:
                people.append((i, j))
                p += 1
            elif array[i][j] > 1:
                stairs.append((i, j))                    
    
    total = float("inf")
    for n in range(N):
        for subgroup1 in combinations(people, n):
            subgroup2 = list(set(people) - set(subgroup1))
            time = max(go_for_lunch(subgroup1, stairs[0]), go_for_lunch(subgroup2, stairs[1]))
            total = min(total, time)
    
    print(f"#{tc} {total}")