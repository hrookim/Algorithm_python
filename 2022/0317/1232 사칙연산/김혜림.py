import sys
sys.stdin = open('input.txt')

""" 출력용 함수
def inorder_print(n):
    global operation
    if n:
        if type(tree[n]) == int:
            operation.append(tree[n])
        if tree[n] in ('+', '-', '*', '/'):
            operation.append('(')
            inorder_print(ch1[n])
            operation.append(tree[n])
            inorder_print(ch2[n])
            operation.append(')')
"""


def inorder(n):
    if n:
        if tree[n] in ('+', '-', '*', '/'):
            if type(tree[ch1[n]]) == int and type(tree[ch2[n]]) == int:
                tree[n] = operates(tree[ch1[n]], tree[n], tree[ch2[n]])
            else:
                inorder(ch1[n])
                inorder(ch2[n])
                if tree[ch1[n]] not in ('+', '-', '*', '/') and tree[ch2[n]] not in ('+', '-', '*', '/'):
                    tree[n] = operates(tree[ch1[n]], tree[n], tree[ch2[n]])
        
            
def operates(a, char, b):
    if char == '+':
        return a + b
    elif char == '-':
        return a - b
    elif char == '*':
        return a * b
    elif char == '/':
        return a / b

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for _ in range(N):
        txt = list(input().split())
        if len(txt) == 2:
            tree[int(txt[0])] = txt[1]
        elif len(txt) == 4:
            tree[int(txt[0])] = txt[1]
            ch1[int(txt[0])] = int(txt[2])
            ch2[int(txt[0])] = int(txt[3])
    
    for i in range(1, N+1):
        if tree[i] in ('+', '-', '*', '/'):
            pass
        else:
            tree[i] = int(tree[i])
            
    result = 0
    inorder(1)
    print(f'#{tc} {int(tree[1])}')