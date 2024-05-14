import sys
sys.stdin = open("input.txt")

# https://velog.io/@js43o/%EB%B0%B1%EC%A4%80-12865%EB%B2%88-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD

# 여행에 필요한 물건 N개
# 각 물건은 무게 W와 가치 V -> 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있음
# 준서는 K만큼의 무게만을 넣을 수 있는 배낭있음
# 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값

N, K = map(int, input().split())

items = []

for _ in range(N):
    items.append(list(map(int, input().split())))
    
# 2차원 DP를 생각하는 것
# DP라는 것은 현재의 최적값이 과거의 최적값을 통해 설명될 수 있어야 하는 것이다..
# 그런데 기준을 하나만 두어서는 점화식을 만드는 것이 불가능하다 이말이야~

# 조건을 2개로 두고 산출을 해보자!!
# 최대 중량을 행으로, 아이템의 인덱스를 열로 두고 계산을 해보자

dp_matrix = [[0]*(N+1) for _ in range(K+1)]
# dp_matrix[i][j]는 최대 무게가 i일때, j번째 아이템까지 살펴봤을 때의 최대 가치
# dp_matrix[i] 배열과 dp_matrix[j] 배열의 값은 항상 0이다..!
# 아이템 0개로 구성 X, 최대무게 0kg 만들기 X

for i in range(1, K+1):
    for j in range(1, N+1):
        item_w, item_v = items[j-1]
        # print(item_w, item_v)
        if i - item_w >= 0:
            dp_matrix[i][j] = max(dp_matrix[i - item_w][j - 1] + item_v, dp_matrix[i][j - 1])
        else:
            dp_matrix[i][j] = dp_matrix[i][j - 1]

result = 0
for k in range(K+1):
    if result < max(dp_matrix[k]):
        result = max(dp_matrix[k])

print(result)