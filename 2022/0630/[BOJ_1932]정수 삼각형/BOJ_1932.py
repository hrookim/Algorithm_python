import sys 
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

N = int(input())

tri = []
for _ in range(N):
    nums = list(map(int, input().split()))
    tri.append(nums)

for i in range(N-2, -1, -1):
    for j in range(i+1):
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])

print(tri[0][0])        
        
    