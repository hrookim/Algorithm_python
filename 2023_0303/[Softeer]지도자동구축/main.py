import sys
sys.stdin = open('input.txt') 

input = sys.stdin.readline

N = int(input())

array = [2] + [0] * 16

for idx in range(1, 17):
    array[idx] = array[idx-1] + 2**(idx-1)

print(array[N] ** 2)