import sys
sys.stdin = open('input.txt')

N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

matrix = [[0]*100 for _ in range(100)]

for point in points:
    for i in range(point[0], point[0]+10):
        for j in range(point[1], point[1] + 10):
            matrix[i][j] += 1

total = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j]:
            total += 1

print(total)