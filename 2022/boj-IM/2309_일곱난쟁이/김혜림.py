import sys
sys.stdin = open('input.txt')


def find_dwarf(heights):
    
    for i in range(N - 1):
        for j in range(i + 1, N):
            total = sum(heights)
            total -= (heights[i] + heights[j])

            if total == 100:
                heights[i] = 0
                heights[j] = 0
                return heights
            
            
N = 9

heights = [int(input()) for _ in range(N)] 

result = find_dwarf(heights)
result.sort()

for num in result:
    if num != 0:
        print(num)
    