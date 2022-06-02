# 50% 정답 -> 시간 초과

import sys 
from itertools import permutations
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    word = list(input().rstrip())
    word_len = len(word)
    anagram = sorted(set(permutations(word, word_len)))
    
    for ana in anagram:
        print(''.join(ana))
    
    