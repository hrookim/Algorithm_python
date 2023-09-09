import sys 
sys.stdin = open('input1.txt') 

N = int(input())
M = int(input())

VIPs = list()
for _ in range(M):
    vip = int(input())
    VIPs.append(vip)
    

dp = [1] * (N+2)
dp[1], dp[2] = 1, 2

for i in range(3, N+2):
    dp[i] = dp[i-1] + dp[i-2]

result = 1
pre_vip = 0
if VIPs:
    for vip in VIPs:
        n = vip - pre_vip - 1
        pre_vip = vip
        result *= dp[n]
    result *= dp[N-vip]

else:
    result *= dp[N]

print(result)
    
