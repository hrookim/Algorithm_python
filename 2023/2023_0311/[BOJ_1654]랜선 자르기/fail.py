import sys 
sys.stdin = open('input2.txt') 

K, N = map(int, input().split())

lens = []
for _ in range(K):
    n = int(input())
    lens.append(n)

min_len = min(lens)
max_N_len = 0
left, right = 1, min_len
while left <= right:
    mid = (left + right) // 2
    
    tmp = 0
    for len in lens:
        tmp += len // mid
    
    if tmp == N and mid > max_N_len:
        max_N_len = mid
        left = mid + 1
    elif tmp < N:
        right = mid - 1
    else:
        left = mid + 1

print(max_N_len)