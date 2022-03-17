import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = round(N**(1/3), 4)
    if n.is_integer():
        print(f'#{tc} {int(n)}')
    else:
        print(f'#{tc} -1')