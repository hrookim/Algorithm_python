"""
n개의 정점을 갖는 이진 트리 -> 1~n 중복없이 번호 있음.
inorder와 postorder가 주어졌을 때, 프리오더를 구하는 프로그램
input:
n
인오더를 나타내는 n개의 자연수
포스트오더를 나타내는 n개의 자연수
"""
import sys
sys.stdin = open('input2.txt')


def preorder(n):
    global answer
    if n:
        answer.append(tree[n])
        if 2*n <= N:
            preorder(2*n)
        if 2*n+1 <= N:
            preorder(2*n+1)
        

def make_tree_post(numbers, root):
    global tree
    if len(numbers) == 0:
        return
    if len(numbers) == 1:
        cr = numbers.pop()
        root = root * 2 + 1
        if not tree[root]:
            tree[root] = cr
        else: 
            tree[root - 1] = cr
    else:
        r = numbers[-1]
        new_ri = numbers.index(r)
        new_lefts = postz[:new_ri]
        make_tree_post(new_lefts, 2*root)
        new_rights = postz[new_ri:-1]
        make_tree_post(new_rights, 2*root+1)


N = int(input())
inz = list(map(int, input().split()))
postz = list(map(int, input().split()))

tree = [0] * (2*N)
tree[1] = postz[-1]

if len(inz) == 1:
    print(*inz)
else: 
    make_tree_post(postz, 1)
    
    answer = []
    preorder(1)
    print(*answer)