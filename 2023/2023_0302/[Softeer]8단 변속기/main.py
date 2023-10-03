import sys 
sys.stdin = open('input.txt') 

input = sys.stdin.readline

numbers = list(map(int, input().split()))
L = 8

result = ""
if numbers[0] == 1 and numbers[L - 1] == 8:
    l = 0
    is_ascending = True
    while l < L - 1:
        if numbers[l] + 1 == numbers[l + 1]:
            l += 1
        else:
            is_ascending = False
            result = 'mixed'
            break

    if is_ascending: result = "ascending"

elif numbers[0] == 8 and numbers[L - 1] == 1:
    l = 0
    is_descending = True
    while l < L - 1:
        if numbers[l] - 1 == numbers[l + 1]:
            l += 1
        else:
            is_descending = False
            result = 'mixed'
            break

    if is_descending: result = "descending"
else:
    result = 'mixed'

print(result)


