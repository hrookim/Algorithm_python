# 완전이진트리
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L이 주어지고, 다음 줄부터 M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    
    for i in range(N, 0, -1):
        tree[i//2] += tree[i]
    
    print(f'#{tc} {tree[L]}')
    
