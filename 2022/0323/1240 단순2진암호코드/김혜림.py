# 배열 > 암호코드 1개 존재
# 암호코드: 가로 7 * 8칸으로 구성
import sys
sys.stdin = open('input.txt')

decoding = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9    
}

T = int(input())

for tc in range(1, T+1):
    # 세로 N 가로 M
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    
    check = []
    for i in range(N):
        if '1' in matrix[i]:
            check = matrix[i]
            for idx in range(M - 1, 0, -1):
                if check[idx] == '1':
                    check = check[idx - 55:idx+1]
                    break
            break
    
    codes = []
    for j in range(8):
        a = ''.join(check[7*j:7*(j+1)])
        codes.append(a)
        codes[j] = decoding[codes[j]]
    
    total = 0
    for i in range(4):
        total += codes[2*i]*3 + codes[2*i+1]
        
    print(f'#{tc} {sum(codes)}') if total % 10 == 0 else print(f'#{tc} 0')