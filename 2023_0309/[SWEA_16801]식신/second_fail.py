import sys
import heapq
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 사람과 음식의 수, 트레이닝 횟수
    performances = list(map(int, input().split()))
    foods = list(map(int, input().split()))

    performances.sort(reverse=True)
    foods.sort()

    tree = []
    for i in range(N):
        tree.append((-performances[i] * foods[i], performances[i], foods[i]))
    heapq.heapify(tree)
    for k in range(K):
        max_score, max_p, max_f = heapq.heappop(tree)
        if max_p > 0:
            max_p -= 1
            heapq.heappush(tree, (-max_p * max_f, max_p, max_f))

        else:
            break

    print(f"#{tc} {-tree[0][0]}")


