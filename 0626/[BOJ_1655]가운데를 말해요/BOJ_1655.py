import sys 
sys.stdin = open('input1.txt') 
input = sys.stdin.readline
N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
    
    # 홀수길이
    l = len(numbers)
    if l % 2:
        print(sorted(numbers)[l//2])
    # 짝수길이
    else:
        print(sorted(numbers)[l//2-1])
