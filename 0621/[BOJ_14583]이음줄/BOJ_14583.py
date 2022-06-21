import sys 
sys.stdin = open('input1.txt') 

# 가로, 세로
H, V = map(float, input().split())

# 대각선 길이
d = (H**2 + V**2)**0.5
c = d - H
a = (V**2 - c**2) / (2*V)
b = (H**2 + a**2)**0.5
h = (H*V - H*a) / b

print(round(0.5*b, 2), round(h, 2))