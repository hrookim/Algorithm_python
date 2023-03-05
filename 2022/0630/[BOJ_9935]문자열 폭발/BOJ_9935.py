# 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 
# 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
# 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
# 남아있는 문자열이 없는 경우 "FRULA"
# 48% 성공

import sys 
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

strs = input().strip()
bomb = input().strip()

while True:
    test = ''.join(strs.split(bomb))
    if strs == test:
        break
    elif test == '':
        strs = 'FRULA'
    else:
        strs = test
print(strs)
