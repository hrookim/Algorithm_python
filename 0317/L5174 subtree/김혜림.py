import sys
sys.stdin = open("input.txt")


def get_node_num(N):
    global result
    if ch1[N]:
        result += 1
        get_node_num(ch1[N])
    if ch2[N]:
        result += 1
        get_node_num(ch2[N])
        
    
T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    numbers = list(map(int, input().split()))
    ch1 = [0] * (E + 3)  # 정점의 개수 == E + 1
    ch2 = [0] * (E + 3)
    for i in range(E):
        p, c = numbers[i*2], numbers[i*2+1]
        if not ch1[p]:
            ch1[p] = c
        else:
            ch2[p] = c
    
    result = 1
    get_node_num(N)
    
    print(f'#{tc} {result}')
        