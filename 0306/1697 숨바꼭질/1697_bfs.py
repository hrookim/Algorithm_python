import sys
from collections import deque
sys.stdin = open("input.txt")


def move(current):
    global K
    visited = [0] * 100001

    q = deque([current])
    
    while q:
        c = q.popleft()
        
        if c == K:
            return visited[c]
        for i in [c+1, c*2, c-1]:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[c] + 1
                q.append(i)
    
    
N, K = map(int, input().split())
print(move(N))