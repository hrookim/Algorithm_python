import sys
sys.stdin = open('input.txt')

def DFS(row, col, number):
    to_visits = [[row, col]]

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current_row, current_col = to_visits.pop()
        number += matrix[current_row][current_col]

        if len(number) == 7:
            if number not in numbers:
                numbers.append(number)
            return
        # 여기에 넣어야 PASS가 됨. 따로 빼니까 PASS가 안되고 시간초과가 남.
        for i in range(4):
            w = current_row+dxs[i]
            h = current_col+dys[i]
            if 0<=w<4 and 0<=h<4 and len(number) <= 6:
                DFS(w, h, number)




T = int(input())
for tc in range(1, T+1):
    numbers = []
    matrix = [list(input().split()) for _ in range(4)]
    number = ''
    cnt = 0
    for row in range(4):
        for col in range(4):
            DFS(row, col, number)
    print(f'#{tc}', len(numbers))
