import sys
sys.stdin = open('input.txt')


def find_w_b(x, y, N):
    global white, blue
    # 분할
    tmp = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[i][j]:
                tmp += 1
    if tmp == 0:
        white += 1
    elif tmp == N**2:
        blue += 1
    else:
        find_w_b(x, y, N//2)
        find_w_b(x+N//2, y, N//2)
        find_w_b(x, y+N//2, N//2)
        find_w_b(x+N//2, y+N//2, N//2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

find_w_b(0, 0, N)
print(white)
print(blue)