import sys
sys.stdin = open("input.txt")

W, N = map(int, input().split())

metals = [list(map(int, input().split())) for _ in range(N)]

# 0. 금속을 비싼값대로 정렬
metals.sort(key=lambda x: -x[1])

# 1. 값비싼 것부터 넣기
max_price = 0
idx = 0
while W > 0:
    current_metal_wegith = metals[idx][0]
    current_metal_price = metals[idx][1]
    if W >= current_metal_wegith:
        max_price += current_metal_wegith * current_metal_price
        W -= current_metal_wegith
    else:
        max_price += W * current_metal_price
        W -= current_metal_wegith
    idx += 1

print(max_price)
