import sys 
sys.stdin = open('input1.txt') 

formula = list(input().strip())

check = [0] * len(formula)
s = 1
for idx in range(len(formula)):
    if formula[idx] == '(':
        