import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = sorted(list(map(int, input().split())))

memo = [0] * N

for i in range(N):
    for j in range(i, N):
        memo[j] += numbers[i]

print(sum(memo))