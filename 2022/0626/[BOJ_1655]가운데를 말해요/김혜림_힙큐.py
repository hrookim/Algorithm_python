import heapq, sys
sys.stdin = open('input1.txt') 
input = sys.stdin.readline
N = int(input())

left = []   # 최대힙
right = []  # 최소힙
answer = []

for _ in range(N):  
    n = int(input())
    # 홀수
    if len(left) == len(right):
        heapq.heappush(left, (-n, n))
    else:   # 짝수
        heapq.heappush(right, (n, n))
    if right and left[0][1] > right[0][1]:
        min_n = heapq.heappop(right)[1]
        max_n = heapq.heappop(left)[1]
        heapq.heappush(left, (-min_n, min_n))
        heapq.heappush(right, (max_n, max_n))
    
    answer.append(left[0][1])

for i in answer:
    print(i)

