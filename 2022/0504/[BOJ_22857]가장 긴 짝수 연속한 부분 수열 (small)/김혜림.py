"""공부 후 작성해본 코드"""

import sys 
sys.stdin = open('input1.txt') 
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

odd_cnt = even_cnt_max = e = size = 0

if N == 1:
    print(0) if numbers[0] % 2 else print(1)
else:
    for s in range(N):
        # 0. 이미 e는 끝지점에 도착했는가?
        if e < N-1:
            # 1. s -> e: 홀수가 K개 될때까지 없애면서 부분수열 만들기
            while odd_cnt <= K:
                # 홀수일 경우
                if numbers[e] % 2 == 1:
                    if odd_cnt == K:
                        break
                    odd_cnt += 1
                    size += 1
                # 짝수일 경우
                else:
                    size += 1
                
                # e가 끝지점에 도달했을때의 처리과정
                if e <= N-2:
                    e += 1
                elif e == N-1:
                    break
            
        # 2. 짝수인 최장부분수열 갱신
        if size - odd_cnt > even_cnt_max:
            even_cnt_max = size - odd_cnt
        
        # 3. s가 다음으로 넘어가면 size가 하나 줄어든다!
        size -= 1
        if numbers[s] % 2 == 1:
            odd_cnt -= 1
    print(even_cnt_max)