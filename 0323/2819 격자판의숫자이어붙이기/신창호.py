import sys

sys.stdin = open('input.txt')


def func(r, c, string):
    global answer
    if len(string) == 7:
        answer.add(string)
        return

    for d in range(4):
        new_r = r + drs[d]
        new_c = c + dcs[d]
        if 0 <= new_r < 4 and 0 <= new_c < 4:
            func(new_r, new_c, string + matrix[new_r][new_c])


T = int(input())
for tc in range(1, T + 1):
    matrix = [list(input().split()) for _ in range(4)]

    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]

    answer = set()
    for i in range(4):
        for j in range(4):
            func(i, j, matrix[i][j])
    print(f'#{tc}', len(answer))
