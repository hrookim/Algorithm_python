import sys 
sys.stdin = open('input1.txt') 

input = sys.stdin.readline
H, W, X, Y = map(int, input().split())
mixed_arr = [list(map(int, input().split())) for _ in range(H+X)]

original_arr = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        original_arr[i][j] = mixed_arr[i][j]

for i in range(X, H):
    for j in range(Y, W):
        original_arr[i][j] -= original_arr[i-X][j-Y]
 
for arr in original_arr:
    print(*arr)