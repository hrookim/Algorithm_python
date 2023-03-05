import sys
sys.stdin = open('input1.txt')

sentence = list(input().strip())

answer, i = 1, 1
orders = {'w': 'o', 'o': 'l', 'l': 'f', 'f': 'w'}
cnt = [1]

if sentence[0] == 'w' and sentence[-1] == 'f':
    while i < len(sentence):
        if sentence[i - 1] == sentence[i]:
            cnt[-1] += 1
        else:
            if sentence[i] == 'w' and len(cnt) >= 4:
                if cnt[-1] == cnt[-2] == cnt[-3] == cnt[-4]:
                    cnt.append(1)
                else:
                    answer = 0
                    break
            elif orders[sentence[i - 1]] == sentence[i]:
                cnt.append(1)
            else:
                answer = 0
                break
        i += 1
    else:
        if len(cnt) < 4 or len(cnt) % 4:
            answer = 0
        elif cnt[-1] == cnt[-2] == cnt[-3] == cnt[-4]:
            pass
        else:
            answer = 0
else:
    answer = 0
print(answer)