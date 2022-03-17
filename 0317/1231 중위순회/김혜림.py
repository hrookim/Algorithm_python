import sys
sys.stdin = open('input.txt')


def inorder(n):
    global orders
    
    if n:
        inorder(ch1[n])
        orders.append(tree[n])
        inorder(ch2[n])
    
    
T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for _ in range(N):
        text = list(input().split())
        if len(text) == 2:
            tree[int(text[0])] = text[1]
        elif len(text) == 3:
            tree[int(text[0])] = text[1]
            ch1[int(text[0])] = int(text[2])
        else:
            tree[int(text[0])] = text[1]
            ch1[int(text[0])] = int(text[2])
            ch2[int(text[0])] = int(text[3])
    
    orders = []
    inorder(1)
    answer = ''.join(orders)
    print(f'#{tc} {answer}')
