import sys
from collections import deque
sys.stdin = open('input2.txt') 

input = sys.stdin.readline


def update_dice(move, ci, cj):
    global dice, array
    
    if move == "right":
        dice["top"], dice["right"], dice["bottom"], dice["left"] \
            = dice["left"], dice["top"], dice["right"], dice["bottom"]
    elif move == "left":
        dice["top"], dice["right"], dice["bottom"], dice["left"] \
            = dice["right"], dice["bottom"], dice["left"], dice["top"]
    elif move == "up":
        dice["top"], dice["front"], dice["bottom"], dice["back"] \
            = dice["front"], dice["bottom"], dice["back"], dice["top"]
    elif move == "down":
        dice["top"], dice["front"], dice["bottom"], dice["back"] \
            = dice["back"], dice["top"], dice["front"], dice["bottom"]
    
    if array[ci][cj]:
        dice["bottom"] = array[ci][cj]
        array[ci][cj] = 0
    else:
        array[ci][cj] = dice["bottom"]

# 세로, 가로, _ , _ , 명령의 개수
N, M, X, Y, K = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

commands = deque(list(map(int, input().split())))

directions = {
    1: [(0, 1), "right"],  # 동
    2: [(0, -1), "left"],  # 서
    3: [(-1, 0), "up"],    # 북
    4: [(1, 0), "down"]    # 남
}

# 0. 주사위 초기화
dice = {
    "top": 0,
    "bottom": 0,
    "left": 0,
    "right": 0,
    "front": 0,
    "back": 0
}

# 1. 명령어를 실행하면서 주사위를 굴리고, 결과를 출력한다.
results = []
ci, cj = X, Y
while commands:
    current_command = commands.popleft()
    
    di, dj = directions[current_command][0] 
    move = directions[current_command][1]
    if 0 <= ci + di < N and 0 <= cj + dj < M:
        ci += di
        cj += dj
        update_dice(move, ci, cj)
        print(dice["top"])


