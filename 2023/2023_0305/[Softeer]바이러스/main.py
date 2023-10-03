import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

# 처음 바이러스 수 / 증가율 / 총 시간
K, P, N = map(int, input().split())

virus = K
for i in range(N):
    virus *= P
    virus %= 1000000007

print(virus)