import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    # 0. 약수를 찾을 때! 제곱수 이하에서만 찾으면 된다.
    n = int(N ** 0.5) + 1
    divisor_list = []
    for q in range(1, n):
        if N % q == 0:
            divisor_list.append((q, N//q))
    
    start = (1, 1)
    min_move = float("inf")
    for divisor in divisor_list:
        tmp_move = divisor[0]-start[0] + divisor[1]-start[1]
        if tmp_move < min_move:
            min_move = tmp_move
    
    print(f"#{tc} {min_move}")