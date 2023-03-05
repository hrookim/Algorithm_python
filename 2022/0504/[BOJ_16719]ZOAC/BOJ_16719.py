"""
아직 보여주지 않은 문자 중 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 하는 문자를 보여주는 것이다.
"""

import sys 
sys.stdin = open('input1.txt') 

word = list(input())
word_len = len(word)

# 1. 필요한 정보를 담은 새로운 리스트 생성
word_ascii = []
for i in range(word_len):
    word_ascii.append([word[i], i, ord(word[i])])


def find_next_char(l, r):
    global visited, word_ascii, tmp
    # 종료조건
    if l+1 == r:
        return 
    # 그 중 사전순서 가장 앞인거 찾기
    min_ascii = next_idx = 200
    for idx in range(l+1, r):
        if word_ascii[idx][2] < min_ascii:
            min_ascii = word_ascii[idx][2]
            next_idx = word_ascii[idx][1]
    add_and_print(word_ascii[next_idx])
    find_next_char(next_idx, r)
    find_next_char(l, next_idx)
    

def add_and_print(context):
    global tmp
    tmp.append(context)
    tmp.sort(key=lambda x: x[1])
    answer = list(map(list, zip(*tmp)))
    print(''.join(answer[0]))
    

tmp = []
find_next_char(-1, word_len)

