import sys 
sys.stdin = open('input1.txt') 

N = int(input())
array = [list(map(int, list(input().rstrip()))) for _ in range(N)]


def DFS(i, j):
    global visited, array
    result = 0
    
    stack = [(i, j)]
    while stack:
        ci, cj = stack.pop()
        result += 1
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and array[ni][nj] and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    
    return result
    
    

apt_dict = dict()
total_apt = 0

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if array[i][j] and not visited[i][j]:
            total_apt += 1
            visited[i][j] = 1
            current_apt = DFS(i, j)
            
            apt_dict[total_apt] = current_apt

print(total_apt)

for s in sorted(apt_dict.values()):
    print(s)