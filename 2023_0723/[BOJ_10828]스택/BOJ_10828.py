import sys
sys.stdin = open('input1.txt') 
input = sys.stdin.readline


def stack_command(cmd):
    global stack
    c = cmd[0]
    l = len(stack)
    if c == "push":
        stack.append(cmd[1])
    elif c =="pop":
        if l > 0:
            print(stack.pop())
        else:
            print(-1)
    elif c == "size":
        print(l)
    elif c == "empty":
        if l == 0:
            print(1)
        else:
            print(0)
    elif c == "top":
        if l > 0:
            print(stack[-1])
        else:
            print(-1)


N = int(input())
stack = []

for _ in range(N):
    current_cmd = list(input().split())
    stack_command(current_cmd)