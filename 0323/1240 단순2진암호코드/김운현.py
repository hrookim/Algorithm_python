import sys
sys.stdin = open('input.txt')

nums = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,}

def extracting_password(arr):
    global col, row, password
    for y in range(col):
        for x in range(row-1, -1, -1):
            if arr[y][x] == '1':
                password = arr[y][x-55:x+1]
                return password

T = int(input())

for tc in range(1, T+1):
    col, row = map(int, input().split())
    matrix = [input() for _ in range(col)]
    password = ''
    extracting_password(matrix)
    result = []
    start_idx = 0
    end_idx = 6
    for i in range(8):
        result.append(nums[password[start_idx:end_idx+1]])
        start_idx += 7
        end_idx += 7

    code = ((result[0] + result[2] + result[4] + result[6]) * 3) + (result[1] + result[3] + result[5]) + result[7]

    if code % 10 == 0:
        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} 0')
