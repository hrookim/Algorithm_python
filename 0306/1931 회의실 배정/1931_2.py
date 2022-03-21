import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))
    
    
meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

cnt = 0
prev_et = 0  # previous endtime
for meeting in meetings:
    st, et = meeting[0], meeting[1]
    
    if st >= prev_et:
        cnt += 1
        prev_et = et

print(cnt)
