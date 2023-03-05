import sys
sys.stdin = open('input.txt')


def find_surface(field):
    # 전체 넓이를 찾기 위해 밑변, 높이 길이 찾기
    h = []
    w = []
    for point in field:
        if point[0] in (3, 4):
            h.append(point[1])
        elif point[0] in (1, 2):
            w.append(point[1])

    total_s = max(h) * max(w)

    # 빼야 할 구간 찾기
    while True:
        if field[0][0] == field[2][0] and field[1][0] == field[3][0]:
            break
        else:
            field = field[1:] + [field[0]]

    abstraction = field[1][1] * field[2][1]

    return total_s - abstraction


K = int(input())  # 1제곱미터에 제배되는 참외

field = [list(map(int, input().split())) for _ in range(6)]

print(find_surface(field)*K)



    
    