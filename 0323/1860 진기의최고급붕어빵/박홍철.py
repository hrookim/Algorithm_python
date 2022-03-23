import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()

    for i in range(N):
        if (customers[i] // M) * K < i + 1:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')
