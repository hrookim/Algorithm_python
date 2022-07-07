import sys 
from fractions import Fraction
sys.stdin = open('input1.txt') 

n, m = map(int, input().split())

answer = 1
for i in range(n, n-m, -1):
    answer *= Fraction(i, (n-i+1))

print(int(answer))