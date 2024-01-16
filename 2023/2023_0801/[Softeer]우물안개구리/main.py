import sys

input = sys.stdin.readline

# 자신이 최고라고 생각하는 회원이 몇명인지?

N, M = map(int, input().split())

members = [0] + list(map(int, input().split()))

relations = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, input().split())

    relations[A].append(B)
    relations[B].append(A)

result = 0
for m, rivals in relations.items():
    current_weight = members[m]
    is_best = True
    for rival in rivals:
        if current_weight <= members[rival]:
            is_best = False
            break

    if is_best:
        result += 1

print(result)
