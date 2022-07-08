import sys

sys.stdin = open('input1.txt')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))