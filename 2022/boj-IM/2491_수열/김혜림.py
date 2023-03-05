import sys
sys.stdin = open('input1.txt')


def get_seq_length(N, numbers):
    max_len = 1

    up = 1
    for i in range(1, N):
        if numbers[i - 1] <= numbers[i]:
            up += 1
            max_len = up if up > max_len else max_len
        else:
            up = 1

    down = 1
    for i in range(1, N):
        if numbers[i - 1] >= numbers[i]:
            down += 1
            max_len = down if down > max_len else max_len
        else:
            down = 1

    return max_len
            

N = int(input())
numbers = list(map(int, input().split()))

print(get_seq_length(N, numbers))