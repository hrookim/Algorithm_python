import sys
sys.stdin = open('input.txt')

numberset =['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

def Convert(codes):
    for j in range(len(codes)):
        for i in range(len(numberset)):
            if codes[j] == [numberset[i]]:
                codes[j] = i
    return codes

def Verify(codes):
    odd, even = 0, 0
    for i in range(len(codes)-1):
        if i%2 == 0: # 홀수
            odd += codes[i]
        else: # 짝수
            even += codes[i]
    result = odd*3 + even + codes[-1]
    if result % 10 == 0: # 10의 배수이면
        return odd+even+codes[-1]
    else:
        return 0

# 입력
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [ input() for _ in range(N) ]
    flag = 0

    # 코드 찾아오기
    code = []
    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == '1':
                code.append(arr[i][j-55:j+1])
                flag = 1
                break
        if flag:
            break

    # 코드 7개씩 나누기
    codes = []
    for c in range(0,len(code[0]),7):
        codes.append([code[0][c:c+7]])

    # 코드 숫자로 변환
    Convert(codes)

    # 출력
    print(f'#{tc} {Verify(codes)}')