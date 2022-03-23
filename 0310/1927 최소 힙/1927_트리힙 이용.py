import sys
sys.stdin = open('input.txt')


def sort_heap():
    global last
    tmp = last
    # 부모와 비교
    while tmp > 1 and tree[tmp]:
        if tree[tmp // 2] > tree[tmp]:
            tree[tmp], tree[tmp // 2] = tree[tmp // 2], tree[tmp]
            tmp //= 2
        else:
            tmp //= 2

    
N = int(input())
operations = [int(input()) for _ in range(N)]

tree = [0] * (N + 1)
last = 1
for op in operations:
    if op == 0:
        if tree[1] == 0:
            print(0)
        else:
            print(tree[1])
            tree = [0] + tree[2::]
            last -= 2
            sort_heap()
    else:
        tree[last] = op
        sort_heap()
        last += 1
        