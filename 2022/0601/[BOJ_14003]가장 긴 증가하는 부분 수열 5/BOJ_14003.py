import sys
from bisect import bisect_left
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

nINF = -float('inf')

N = int(input())
numbers = list(map(int, input().split()))

lis_stack = [nINF]
lis_total = [(nINF, 0)]

for num in numbers:
    if num > lis_stack[-1]:
        lis_stack.append(num)
        lis_total.append((num, len(lis_stack)-1))
    else:
        idx = bisect_left(lis_stack, num)
        lis_stack[idx] = num
        lis_total.append((num, idx))

answer = []
lis_length = len(lis_stack) - 1
while lis_total and lis_length:
    n, i = lis_total.pop()
    if i == lis_length:
        answer.append(n)
        lis_length -= 1

print(len(answer))
print(*answer[::-1])

