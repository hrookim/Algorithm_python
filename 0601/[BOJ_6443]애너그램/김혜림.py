# 백트랙킹 과정이 포함된 풀이! 
# 딕셔너리 사용하기
import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline


def DFS(l, chars, perm):
    global word, word_len, answer
    # 1. 종료조건
    if l == word_len:
        answer.add(perm)
        print(perm)
    # 2. 순열
    if perm not in answer:
        answer.add(perm)
        for i in range(len(chars)):
            DFS(l+1, chars[:i]+chars[i+1:], perm+chars[i])


N = int(input())

for _ in range(N):
    word = sorted(input().rstrip())
    word_len = len(word)
    answer = set()
    DFS(0, word, '')
