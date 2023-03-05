import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


M = int(input())

S = set()
for _ in range(M):
    inputs = list(input().split())
    # 숫자로 바꿔주기
    if len(inputs) == 2:
        inputs[1] = int(inputs[1])
        
    if inputs[0] == 'add':
        S.add(inputs[1])
    elif inputs[0] == 'remove':
        s = [inputs[1]]
        S -= set(s)
    elif inputs[0] == 'check':
        print(1) if inputs[1] in S else print(0)
    elif inputs[0] == 'toggle':
        if inputs[1] in S:
            s = [inputs[1]]
            S -= set(s)
        else:
            S.add(inputs[1])
    elif inputs[0] == 'all':
        S = set(range(1, 21))
    elif inputs[0] == 'empty':
        S = set()