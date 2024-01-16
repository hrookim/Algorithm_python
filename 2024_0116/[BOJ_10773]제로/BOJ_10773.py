import sys 
sys.stdin = open('input2.txt') 

K = int(input())

stack = list()

for k in range(K):
    tmp = int(input())
    
    if tmp == 0 and len(stack) > 0:
        stack.pop()
    else:
        stack.append(tmp)

print(sum(stack))
    