import sys
sys.stdin = open('input.txt')


def side_dis(i):
    dis = [[], [W-dg[1]-point[1], point[1]+dg[1]], [dg[1]+H-point[1], W-dg[1]+H-point[1]], [dg[1]+point[1], H-dg[1]+point[1]], [H+W-point[1]-dg[1], W+dg[1]-point[1]]]
    return dis[dg[0]][i]


W, H = map(int, input().split())
S = int(input())
points = [list(map(int, input().split())) for _ in range(S+1)]

# 전처리 과정
for p in points:
    if p[0] in (1, 2):  # 남북인 경우
        p.append('SN')
    else:
        p.append('EW')  # 동서인 경우

dg = points.pop() # 동근이

LR = [[], [4, 3], [3, 4], [1, 2], [2, 1]]
min_dis = 0
for point in points:
    if point[0] == dg[0]:  # 동근이랑 같은 변에 있다면
        min_dis += abs(point[1] - dg[1])
    elif point[2] == dg[2]:   # 동근이의 맞은편 변에 있다면
        if dg[2] == 'SN':
            min_dis += min(point[1] + dg[1] + H, 2 * W - (point[1] + dg[1]) + H)
        elif dg[2] == 'EW':
            min_dis += min(point[1] + dg[1] + W, 2 * H - (point[1] + dg[1]) + W)
    # 동근이의 양옆에 있는 경우
    else:
        for i, side in enumerate(LR[dg[0]]):
            if side == point[0]:
                min_dis += side_dis(i)

print(min_dis)
        

