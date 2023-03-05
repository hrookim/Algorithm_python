import sys
sys.stdin = open('input.txt')

"""
최대 100개의 서로 다른 자연수가 키로 입력
최대힙
"""


# 삽입 연산, n = 키값
def enque(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지

    # 최소 힙 관리
    c = last  # 새로 추가된 정점을 자식으로
    p = c // 2  # 완전이진트리에서의 부모 정점 번호

    # 부모가 있고, 자식의 키 값이 더 크면 교환
    while p >= 1 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0
    
    for num in numbers:
        enque(num)

    n = N
    result = 0
    while n > 1:
        result += tree[n//2]
        n //= 2
    
    print(f'#{tc} {result}')
        