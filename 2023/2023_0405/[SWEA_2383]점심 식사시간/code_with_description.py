import sys
from itertools import combinations
from collections import deque

sys.stdin = open("sample_input.txt")


def go_for_lunch(subgroup, stair):
    global array
    """
    :param subgroup = list 
    :param stair = (i, j) 형태
    """
    stair_level = array[stair[0]][stair[1]]
    # 계단까지 도착하는 시간
    people_time_to_stair = []
    for p in subgroup:
        people_time_to_stair.append(abs(p[0] - stair[0]) + abs(p[1] - stair[1]))

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
        while people_time_to_stair[0] < time:  # 계단까지 도달하는 시간이 현재 시간보다 작으면서
            # (=> 계단에 도달하고 1분 후에 이동이 가능하므로)
            if len(people_on_stair) < 3:  # 계단이 비워져 있다면
                # (계단이 다 차있으면서 이동하지 못한 아이들은 아직 남아있는다)
                people_time_to_stair.popleft()  # 계단으로 이동한다.

                # 마지막 사람이었을 경우, 현재 시간에서 계단 이동시간만큼만 더해주면 된다.
                # 이 경우는 계단에 사람이 있든 없든 상관없다.
                # 계단에 사람들이 있어도, 오름차순 정렬에 따라 가장 마지막 사람이 이 사람이 되므로
                if not people_time_to_stair:
                    time += stair_level
                    break

                # 아직 뒷 사람이 남아있다면, 현재 시간에서 계단 이동시간만큼을 더해서 이동할 것이므로 이를 더해준다.
                people_on_stair.append(time + stair_level)
            else:
                break
    return time


TC = int(input())

for tc in range(1, TC + 1):
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