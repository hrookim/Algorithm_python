import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

N = int(input())  # 악보의 개수
difficulty = [0] + list(map(int, input().split()))  # 악보 번호별 난도
check = [0] * (N + 1)
# 실수할 수 있는 순서를 미리 체크
idx = 1
while idx < N:
    if difficulty[idx] - difficulty[idx + 1] > 0:
        check[idx] += 1
    check[idx] = check[idx-1] + check[idx]
    idx += 1

Q = int(input())
for _ in range(Q):
    # 시작 번호 -> 마지막 번호
    x, y = map(int, input().split())

    print(check[y-1] - check[x-1])




