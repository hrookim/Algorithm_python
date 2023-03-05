# 두 개 이상의 원자가 충돌 할 경우 충돌한 원자들은 각자 보유한 에너지를 모두 방출하고 소멸된다
# 원자들이 소멸되면서 방출하는 에너지의 총합 구하기
import sys
sys.stdin = open('input.txt')

# 상하좌우 0123
dy, dx = (0.5, -0.5, 0, 0), (0, 0, -0.5, 0.5)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # x 위치, y 위치, 이동 방향, 보유 에너지 K
    arr = [list(map(int, input().split())) for _ in range(N)]
    energy = 0
    
    # 0. 최대 이동할 수 있는 시간 동안
    for _ in range(4001):
        if not arr:     # 가지치기
            break
        # 1. 이동하기
        idx = 0
        while idx < len(arr):
            if abs(arr[idx][0]) > 1000 or abs(arr[idx][1]) > 1000:
                arr.pop(idx)
            else:
                arr[idx][0] += dx[arr[idx][2]]
                arr[idx][1] += dy[arr[idx][2]]
                idx += 1

        # 2. 좌표랑 에너지 순으로 내림차순
        arr.sort(key=lambda x: (x[0], x[1], x[3]), reverse=True)
        
        # 3. 충돌하는 경우는 그 인덱스를 따로 저장한 후, 충돌 에너지를 합산한다.
        tmp = -1
        i = 0
        while i < len(arr)-1:
            if arr[i][0] == arr[i+1][0] and arr[i][1] == arr[i+1][1]:
                tmp = i
                arr[i][3] += arr[i+1][3]
                arr.pop(i+1)
            else:
                # 3-1. 합산한 에너지를 저장하면서 원자 없애기
                if tmp >= 0:
                    energy += arr.pop(tmp)[3]
                    tmp = -1
                    continue
                i += 1
        else:
            if tmp >= 0:
                energy += arr.pop(tmp)[3]
    print(f'#{tc} {energy}')
    
    