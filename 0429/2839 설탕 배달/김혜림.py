"""
봉지는 3, 5키로 짜리 있음 최대한 적은 봉지로 들고갈 것!
3 <= N <= 5000
"""
N = 11
answer = 0

# DP 풀이!
if N % 5 == 0:
    answer = N // 5
else:
    while N:
        N -= 3
        answer += 1
        if N % 5 == 0:
            answer += N // 5
            break
        if N < 0:
            answer = -1
            break

print(answer)



# memoization을 이용한 풀이!
memo = []


