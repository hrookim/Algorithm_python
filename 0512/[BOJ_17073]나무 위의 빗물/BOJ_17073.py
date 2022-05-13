import sys 
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

N, W = map(int, input().split())
tree = [[] for _ in range(N+1)] 

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

leaf_nodes = 0
for idx in range(2, N+1):
    if len(tree[idx]) == 1:
        leaf_nodes +=1

print(W/leaf_nodes)