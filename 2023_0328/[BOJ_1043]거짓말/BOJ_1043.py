import sys 
sys.stdin = open('input7.txt') 


def update_true_mans(array):
    global array_true_mans
    for man in array:
        array_true_mans[man] = 1

# 사람의 수, 파티의 수
N, M = map(int, input().split())

# 0-1. 진실을 아는 사람 체크하기
array_true_mans = [0] * 51
true_mans = list(map(int, input().split()))
if len(true_mans) >= 2:
    for i in range(1, len(true_mans)):
        array_true_mans[true_mans[i]] = 1

# 0-2. 파티 저장하기
party = []
for _ in range(M):
    participants = list(map(int, input().split()))
    party.append(participants)

# 1. 파티 돌면서 확인하기            
prev_results = results = M
while True:
    for i in range(M):
        participants = party[i]
        for j in range(1, len(participants)):
            # 1-1. 만약 진실을 듣는 사람이라면, true_mans 업데이트 하기 
            if array_true_mans[participants[j]]:
                results -= 1
                update_true_mans(participants[1:])
                break
    if prev_results == results:
        break
    else: 
        prev_results, results = results, M
    
print(results)