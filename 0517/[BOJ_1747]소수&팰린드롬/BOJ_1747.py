# 어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

import sys 
# sys.stdin = open('input1.txt') 


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


def is_prime(num):
    for q in range(2, int(num ** 0.5)+1):
        if num % q == 0:
            return False
    return True

N = int(input())

if N == 1:
    print(2)
else:
    for n in range(N, 1003002):
        if is_prime(n) and is_palindrome(n):
            print(n)
            break
      
    