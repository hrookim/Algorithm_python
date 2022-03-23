import sys
sys.stdin = open("input.txt")
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def mk_num(row, col, num_string):
    if len(num_string) == 7:
        result_list.append(num_string)
    else:
        for d in range(4):
            if 0 <= row + di[d] < 4 and 0 <= col + dj[d] < 4:
                mk_num(row + di[d], col + dj[d], num_string + board[row + di[d]][col + dj[d]])


T = int(input())

for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]

    result_list = []

    for i in range(4):
        for j in range(4):
            mk_num(i, j, '')

    result = len(list(set(result_list)))

    print(f'#{tc} {result}')
