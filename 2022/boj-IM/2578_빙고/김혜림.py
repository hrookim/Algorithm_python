import sys
sys.stdin = open('input.txt')


def find_bingo():
    cnt = 0
    # 행 탐색
    for i in range(N):
        if False not in visited[i]:
            cnt += 1
    
    # 열 탐색, 전치 행렬 이용
    visited_rev = list(map(list, zip(*visited)))
    
    for j in range(N):
        if False not in visited_rev[j]:
            cnt += 1
    
    # 대각선 탐색
    diag = [[], []]
    for i in range(N):
        diag[0].append(visited[i][i])
        diag[1].append(visited[i][N-1-i])
    
    for k in range(2):
        if False not in diag[k]:
            cnt += 1
            
    if cnt >= 3:
        return True


def check_numbers(matrix, numbers):
    for idx, number in enumerate(numbers):
        for i in range(N):
            for j in range(N):
                if number == matrix[i][j]:
                    visited[i][j] = True
                    if idx >= 11 and find_bingo():
                        return idx+1
                
  
N = 5
matrix = [list(map(int, input().split())) for _ in range(N)]
numbers = []
for i in range(N):
    x = list(map(int, input().split()))
    numbers.extend(x)
    
visited = [[False]*N for _ in range(N)]
    
print(check_numbers(matrix, numbers))


