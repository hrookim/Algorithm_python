import sys
sys.stdin = open('input.txt')


def change_ord(numbers):
    result = [0] * (N+1)
    for i, v in enumerate(numbers):
        left = result[0:i+1-v]
        left.append(i+1)
        right = result[i+1-v:N]
        result = left + right
    
    return result
    
    
N = int(input())

numbers = list(map(int, input().split()))
ans = change_ord(numbers)

print(*ans[1:])
