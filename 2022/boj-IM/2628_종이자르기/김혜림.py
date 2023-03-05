import sys
sys.stdin = open('input.txt')


def get_subset_surface():
    lg = len(garo)+1
    ls = len(sero)+1
    # n = lg*ls if lg and ls else lg+ls
    surfaces = []
    
    xs = [0]*(lg)
    ys = [0]*(ls)

    # 가로 세로 절단선 있을 경우
    if garo and sero:
        for i in range(lg):
            if i == lg-1:
                xs[i] += H - garo[i-1][1]
            elif i >= 1:  # len(garo)가 2 이상이면,
                xs[i] += garo[i][1]-garo[i-1][1]
            else:
                xs[i] += garo[i][1]
        for j in range(ls):
            if j == ls-1:
                ys[j] += W - sero[j-1][1]
            elif j >= 1:  # len(garo)가 2 이상이면,
                ys[j] += sero[j][1]-sero[j-1][1]
            else:
                ys[j] += sero[j][1]
        
        for x in xs:
            for y in ys:
                surfaces.append(x*y)
    
    # 가로 절단선만 있을 경우
    elif garo:
        for i in range(lg):
            if i == lg-1:
                xs[i] += H - garo[i-1][1]
            elif i >= 1:  # len(garo)가 2 이상이면,
                xs[i] += garo[i][1]-garo[i-1][1]
            else:
                xs[i] += garo[i][1]
        
        for x in xs:
            surfaces.append(W*x)
        

    # 세로 절단선만 있을 경우
    elif sero:
        for j in range(ls):
            if j == ls - 1:
                ys[j] += W - sero[j-1][1]
            elif j >= 1:  # len(garo)가 2 이상이면,
                ys[j] += sero[j][1] - sero[j-1][1]
            else:
                ys[j] += sero[j][1]
        
        for y in ys:
            surfaces.append(H*y)
            
    return max(surfaces)
    

W, H = map(int, input().split())
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

garo = []
sero = []
for point in points:
    if point[0] == 0:
        garo.append(point)
    else:
        sero.append(point)

garo.sort()
sero.sort()

print(get_subset_surface())