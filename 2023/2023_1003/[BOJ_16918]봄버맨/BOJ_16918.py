import sys 
sys.stdin = open('input1.txt') 

"""
0: 초기 상태는 봄버맨이 폭탄을 설치해놓은 상태이다. 
1: 아무일도 없음
2: 초기 위치 폭탄 제외한 위치에 폭탄을 놓는다.
3: 3초 전에 설치한 폭탄이 터진다
"""

R, C, N = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(R)]

bomb_arr = [[-1] * C for _ in range(R)]

time = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "O":
            bomb_arr[i][j] = time

if N == 1:
    for i in range(R):
        print(''.join(arr[i]))

elif N % 2 == 0:
    for _ in range(R):
        print("O"*C) 
else:
    time = 2    
    while time <= N:
        
        # 짝수 시간인 경우, 빈칸에 설치
        if time % 2 == 0:
            for i in range(R):
                for j in range(C):
                    if bomb_arr[i][j] == -1:
                        arr[i][j] = "O"
                        bomb_arr[i][j] = time
        # 홀수 시간인 경우, 폭탄 터트리기
        if time % 2 == 1:
            idx_time = time - 3
            for i in range(R):
                for j in range(C):
                    if bomb_arr[i][j] == idx_time:
                        arr[i][j] = "."
                        bomb_arr[i][j] = -1
                        if i+1 < R:
                            arr[i+1][j] = "."
                        if 0 <= i-1:
                            arr[i-1][j] = "."
                        if j+1 < C:
                            arr[i][j+1] = "."
                        if 0 <= j-1:
                            arr[i][j-1] = "."
            for i in range(R):
                for j in range(C):
                    if arr[i][j] == ".":
                        bomb_arr[i][j] = -1
        time += 1

    else:
        for i in range(R):
            print(''.join(arr[i]))