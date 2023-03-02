import sys
sys.stdin = open('input.txt') 

input = sys.stdin.readline

N, M = map(int, input().split())

# 0. 회의실 초기화
meeting_rooms = {}
for _ in range(N):
    meeting_rooms[str(input()).rstrip()] = [0] * 9

# 1. 회의실의 예약된 시간 체크
for _ in range(M):
    room_name, s, e = input().split()

    for t in range(int(s) - 9, int(e) - 9):
        meeting_rooms[room_name][t] = 1

# 2. 가능한 시간 체크
available_rooms = {}
for key, value in meeting_rooms.items():
    available_rooms[key] = []
    available_s, available_e = 10000, -10000
    i = 0
    while i < 9:
        if value[i] == 0:
            if available_s == 10000:
                available_s = i + 9
                available_e = i + 9 + 1
            elif i + 9 > available_s and i + 9 + 1 > available_e:
                available_e = i + 9 + 1
        else:
            if available_s != 10000 and available_e != -10000:
                available_rooms[key].append((available_s, available_e))
            available_s, available_e = 10000, -10000

        i += 1
        if i == 9 and available_s != 10000 and available_e != -10000:
            available_rooms[key].append((available_s, available_e))

# 3. 출력 형태
results = []
for k, v in available_rooms.items():
    results.append([k, len(v), v])

results.sort()
print(results)

for idx in range(N):
    if idx > 0:
        print("-----")
    res = results[idx]
    name = res[0]
    cnt = res[1]
    times = res[2]
    print(f'Room {name}:')
    if cnt > 0:
        print(f'{cnt} available:')
        
        for time in times:
            st = str(time[0]) if time[0] > 9 else '0' + str(time[0])
            et = str(time[1]) if time[1] > 9 else '0' + str(time[1])
            print(f'{st}-{et}')
        
    else:
        print("Not available")
    
    





