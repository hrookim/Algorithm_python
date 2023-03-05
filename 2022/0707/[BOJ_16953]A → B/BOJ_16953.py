# recursion Error 및 메모리 초과 ㅜ

import sys 
sys.stdin = open('input3.txt') 
sys.setrecursionlimit(10 ** 6)
a, b = map(int, input().split())


def find_cnt(number):
    global cnt, a
    # 종료조건
    if number < a:
        cnt = -2
        return

    while number % 2 == 0:
        number //= 2
        cnt += 1
        if number == a:
            return
    else:
        while number % 10 == 1:
            number //= 10
            cnt += 1
            if number == a:
                return
        else:
            find_cnt(number)
    return

cnt = 0
find_cnt(b)
print(cnt+1)
        
        