import sys
sys.stdin = open('input.txt')


def switch_onoff(n):
    if n:       # n이 1일 경우 0으로 바꾸기
        n = 0
    else:       # n이 0일 경우 1로 바꾸기
        n = 1
    return n


def switch_by_student(student, onoff):

    # 남자
    if student[0] == 1:
        for i, v in enumerate(onoff):
            if (i+1) % student[1] == 0:
                onoff[i] = switch_onoff(v)
        return onoff
    
    # 여자
    if student[0] == 2:
        i = student[1]-1
        max_di = 0
        for di in range(0, min(i, len(onoff)-1-i)+1):
            if onoff[i-di] == onoff[i+di]:
                max_di = di
            else:
                break
        
        for idx in range(i-max_di, i+max_di+1):
            onoff[idx] = switch_onoff(onoff[idx])
        
        return onoff
        

# 입력    
S = int(input())
onoff = list(map(int, input().split()))
N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]

for student in students:
    onoff = switch_by_student(student, onoff)

# 출력
while len(onoff) != 0:
    print(*onoff[:20])
    onoff = onoff[20:]
    
