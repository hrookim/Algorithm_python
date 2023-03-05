"""검색코드"""

import sys 
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

oddcnt = 0
start, end = 0, 0
size, evencnt_max = 0, 0
flag = 1

for start in range(n):
    while oddcnt <= k and flag:
        if numbers[end] % 2:
            if oddcnt == k:
                break
            oddcnt += 1
        size += 1
        if end == n - 1:
            flag = 0
            break
        end += 1

    if evencnt_max < size - oddcnt:
        evencnt_max = size - oddcnt

    if numbers[start] % 2:
        oddcnt -= 1

    size -= 1

print(evencnt_max)