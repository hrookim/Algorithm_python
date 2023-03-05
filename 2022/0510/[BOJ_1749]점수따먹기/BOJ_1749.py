# 정수의 합이 최대가 되는 부분행렬을 구하여 빨리 동주에게서 벗어나고 싶다.
# 최대 부분행렬 합 구하기!

import sys 
sys.stdin = open('input1.txt') 

N, M = map(int, input().split())
arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

"""구간합.. 어렵다.... """
for i in range(1, N+1):
    j = 1
    while j <= M:
        arr[i][j] = arr[i][j] + arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]
        j += 1
print(arr)