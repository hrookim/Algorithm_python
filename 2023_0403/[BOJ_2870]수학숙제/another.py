import sys
sys.stdin = open("input3.txt")

# 이렇게 해야만 정답이 된다... 왜..?
input = sys.stdin.readline

N = int(input())

numbers = []
for i in range(N):
    word = input()
    tmp = ''
    for w in word:
        if w.isdigit():  # 숫자라면
            tmp += w
        else:  # 문자라면
            if len(tmp) > 0:
                numbers.append(int(tmp))
            tmp = ''

for number in sorted(numbers):
    print(number)