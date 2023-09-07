import sys 
sys.stdin = open('input1.txt') 

N = int(input())
M = int(input())

seats = [0] * (N+1)
VIPs = list()
for _ in range(M):
    vip = int(input())
    seats[vip] = vip
    VIPs.append(vip)


def find_max(n, current_seats):
    global result, VIPs
    # 0. 종료조건
    if n == N:
        result += 1
        return
    # 1. vip가 앉은 자리라면
    if n in VIPs:
        find_max(n+1, current_seats[::])
    else:
        # 2. 경우의 수
        for k in range(n-1, n+2):
            if k < 1 or k > N: continue
            if not current_seats[k]:
                current_seats[k] = n
                find_max(n+1, current_seats[::])
                current_seats[k] = 0

result = 0
find_max(1, seats[::])
print(result)