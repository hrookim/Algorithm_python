import sys
from collections import deque
sys.stdin = open('input2.txt') 


a, b = map(int, input().split())

def bfs(a, b):
    to_visit = deque([(b, 1)])
    
    while to_visit:
        num, cnt = to_visit.popleft()
        
        if num == a:
            return cnt
        elif num < a:
            return -1
        
        if num % 2 == 0:
            to_visit.append((num//2, cnt+1))
        elif num % 10 == 1:
            to_visit.append((num//10, cnt+1))
        else:
            return -1

print(bfs(a, b))

            