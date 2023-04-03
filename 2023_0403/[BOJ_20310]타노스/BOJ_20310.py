import sys 
sys.stdin = open('input2.txt') 


def is_subtask1():
    global len_S, S
    result = True
    i = 0
    while i+1 < len_S:
        if int(S[i]) == 1 and int(S[i+1]) == 0:
            i += 2
        else:
            return False
    return result


S = input().strip()
len_S = len(S)

if is_subtask1():
    # 1은 앞에서부터 제거 / 0은 뒤에서부터 제거
    removals = [0] * len_S
    i, j = 0, len_S-1
    cnt = 0
    while cnt < len_S / 4:
        removals[i] = 1
        removals[j] = 1
        cnt += 1
        i += 2
        j -= 2
    
    results = ''
    for idx in range(len_S):
        if not removals[idx]:
            results += S[idx]
   
else:
    cnt_1 = cnt_0 = 0
    for s in S:
        if int(s):
            cnt_1 += 1
        else:
            cnt_0 += 1

    removals = [0] * len_S
    i = cnt = 0
    while cnt < cnt_1/2:
        if int(S[i]):
            cnt += 1
            removals[i] = 1
        i += 1
    
    j = len_S-1
    cnt = 0
    while cnt < cnt_0/2:
        if int(S[j]) == 0:
            cnt += 1
            removals[j] = 1
        j -= 1

    results = ''
    for idx in range(len_S):
        if not removals[idx]:
            results += S[idx]
    
print(results)    
    
    
    