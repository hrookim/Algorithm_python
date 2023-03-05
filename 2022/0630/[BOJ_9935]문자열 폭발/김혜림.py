# 성공, 질문검색 코드

import sys 
sys.stdin = open('input2.txt') 
input = sys.stdin.readline

strs = input().strip()
bomb = input().strip()
bomb_l = len(bomb)
bomb_last = bomb[-1]
stack = []

for s in strs:
    stack.append(s)
    if s == bomb_last and ''.join(stack[-bomb_l:]) == bomb:
        for _ in range(bomb_l):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
