import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    inputs = list(map(int, input().split()))

    inputs.sort()

    waits = {}
    cnt = 0
    for i in inputs:
        cnt += 1
        waits[i] = cnt

    flag = 'Possible'
    for time, people in waits.items():
        if (time // M) * K < people:
            flag = 'Impossible'
            break

    print(f'#{tc}', flag)
