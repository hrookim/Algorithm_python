"""
임의의 양의 정수 n에 대해서, 'w'가 n번 나오고, 그 다음에 'o'가 n번, 그 다음에 'l'이 n번, 그 다음에 'f'가 n번 나온 단어는 올바른 단어이다.
올바른 단어 두 개를 이은 단어도 올바른 단어이다.
1번과 2번 조건으로 만들 수 있는 단어만 올바른 단어이다.
71퍼 통과?
"""

import sys 
sys.stdin = open('input1.txt') 

sentence = list(input().strip())

answer, i= 1, 1
orders = {'w': 'o', 'o':'l', 'l':'f', 'f':'w'}
cnt = [1]

while i < len(sentence):
    if sentence[i-1] == sentence[i]:
        cnt[-1] += 1
    else:
        if sentence[i] == 'w' and len(cnt) >= 4:
            if cnt[-1] == cnt[-2] == cnt[-3] == cnt[-4]:
                cnt.append(1)
            else:
                answer = 0 
                break
        if orders[sentence[i-1]] == sentence[i]:
            cnt.append(1)
        else:
            answer = 0
            break
    i += 1
else:
    if len(cnt) < 4:
        answer = 0
    elif cnt[-1] == cnt[-2] == cnt[-3] == cnt[-4]:
        pass
    else:
        answer = 0
    
print(answer)
        
            
        

