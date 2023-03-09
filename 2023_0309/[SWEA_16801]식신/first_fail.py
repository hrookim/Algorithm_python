import sys
sys.stdin = open("input.txt")


def heapq_push(k):
    global tree, last
    # 0. 마지막 원소+1에 새 원소를 넣는다.
    last += 1
    tree[last] = k

    # 1-1. 부모자식 관계 파악을 해서 heap 만들기 위해 이거를 한다.
    c = last
    p = c//2
    
    # 1-2. 부모가 존재하면서 부모보다 큰 애가 자식한테 있다면 바꿔준다. (root 1기준)
    while p > 0 and tree[p][-1] < tree[c][-1]:
        tree[c], tree[p] = tree[p], tree[c]
        c = p
        p = c//2
    

def heapq_pop():
    global last
    # print(last, tree)
    
    # 0. 루트의 값을 잠시 저장한 후, 마지막 값을 루트에 넣는다
    tmp = tree[1]
    tree[1] = tree[last]
    # 1. 마지막 정점이 줄어든다.
    last -= 1
    
    # 2. 부모>자식 규칙 위한 설정 (root부터 훑는다)
    p = 1
    c = 2*p
    
    # 3-1. 우선 마지막까지 다 훑지 않았다면
    while c <= last:
        # 3-2. 우선 오른쪽 자식이 있고 이게 왼쪽 자식보다 크다면 오른쪽 자식을 선택
        if c+1 <= last and tree[c+1][-1] > tree[c][-1]:
            c += 1
        # 3-3. 부모<자식 이라면
        if tree[p][-1] < tree[c][-1]:
            tree[c], tree[p] = tree[p], tree[c]
            p = c
            c = 2*p
        else:
            break
    return tmp
            

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())  # 사람과 음식의 수, 트레이닝 횟수
    performances = list(map(int, input().split()))
    foods = list(map(int, input().split()))
    
    performances.sort(reverse=True)
    foods.sort()

    tree = [(0, 0, 0) for _ in range(N+1)]
    last = 0
    for i in range(N):
        heapq_push((performances[i], foods[i], performances[i]*foods[i]))
    
    for k in range(K):
        max_p, max_f, max_score = heapq_pop()
        if max_p > 0:
            max_p -= 1
            heapq_push((max_p, max_f, max_p*max_f))
        else:
            break
    
    print(f"#{tc} {tree[1][-1]}")
        
        
        