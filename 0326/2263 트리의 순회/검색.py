import sys
sys.stdin = open('input2.txt')

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i


def preorder(istart,iend,pstart,pend):
    if istart > iend or pstart > pend:
        return

    root = postorder[pend]
    print(root,end=' ')

    left_cnt = position[root] - istart
    right_cnt = iend - position[root]

    preorder(istart,position[root]-1,pstart,pstart+left_cnt-1)
    preorder(position[root]+1,iend,pend-right_cnt,pend-1)


preorder(0,n-1,0,n-1)