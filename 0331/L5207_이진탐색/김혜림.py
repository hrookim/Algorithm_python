# 이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.
import sys
sys.stdin = open('input.txt')


def binary(key, numbers, start, end):
    global direction
    if start <= end:
        mid = (start+end) // 2
        if key == numbers[mid]:
            if end == N-1:
                direction = 2
            return True
        elif key < numbers[mid]:
            if direction in (0, 1):
                direction = -1
                return binary(key, numbers, start, mid-1)
        elif key > numbers[mid]:
            if direction in (-1, 0):
                direction = 1
                return binary(key, numbers, mid+1, end)
    else:
        return False
        
        
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nlst = sorted(list(map(int, input().split())))
    mlst = list(map(int, input().split()))
    
    ans = 0
    for m in mlst:
        direction = 0  # 왼쪽으로 가면 -1, 오른쪽으로 가면 1
        if binary(m, nlst, 0, N-1) and direction:
            ans += 1
            
    print(f'#{tc} {ans}')