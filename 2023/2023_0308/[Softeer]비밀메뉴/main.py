import sys

# input = sys.stdin.readline
sys.stdin = open("input1.txt")

# 비밀 메뉴 버튼의 수, 사용자가 누른 버튼의 수, 자판기 총 버튼 수
N, M, K = map(int, input().split())
secret_button = list(map(int, input().split()))
user_button = list(map(int, input().split()))

message = ""
for i in range(M):
    is_secret = False
    if user_button[i] == secret_button[0] and i + N - 1 < M:
        is_secret = True
        for j in range(i + N - 1, i, -1):
            if user_button[j] != secret_button[j - i]:
                is_secret = False
                break

    if is_secret:
        message = "secret"
        break
    else:
        message = "normal"

print(message)
