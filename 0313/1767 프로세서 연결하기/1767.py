import sys
sys.stdin = open('input.txt')


def get_min_line(i, j):
    lines = []
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        line = 0
        ni = i + di
        nj = j + dj
        while matrix[ni][nj] == 0:
            line += 1
            ni += di
            nj += dj
        else:
            if matrix[ni][nj] == 2:
                if line == 0:
                    continue
                else:
                    line += 1
                    lines.append(line)
                
            elif matrix[ni][nj] == 1:
                continue
        
    return lines


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[2]*(N+2)] + [[2] + list(map(int, input().split())) +[2] for _ in range(N)] + [[2]*(N+2)] 
    
    numbers = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] == 1:
                numbers += get_min_line(i, j)
    
    print(numbers)