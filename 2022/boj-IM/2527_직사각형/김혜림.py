import sys
sys.stdin = open('input.txt')

T = 4

for tc in range(T):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # s_points1 = [(x1, y1), (x1, q1), (p1, y1), (p1, q1)]
    # s_points2 = [(x2, y2), (x2, q2), (p2, y2), (p2, q2)]
    
    matrix = [[0]*(max(p1, p2)+1) for _ in range(max(q1, q2)+1)]
    
    # 사각형 칠하기?
    for j in range(x1, p1+1):
        for i in range(y1, q1+1):
            matrix[i][j] += 1
    
    for j in range(x2, p2+1):
        for i in range(y2, q2+1):
            matrix[i][j] += 1
    
    if 2 not in matrix:
        print('d')
    
