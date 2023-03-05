import sys 
sys.stdin = open('input1.txt') 
input = sys.stdin.readline
N = int(input())

points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

print(points)

surface = 0
for i in range(N):
    if i == N-1:
        x1, y1 = points[i][0], points[i][1]
        x2, y2 = points[0][0], points[0][1]
        surface += (x1 * y2) - (x2 * y1)
        continue
    x1, y1 = points[i][0], points[i][1]
    x2, y2 = points[i+1][0], points[i+1][1]
    surface += (x1 * y2) - (x2 * y1)

print(round(abs(surface) * 0.5, 1))