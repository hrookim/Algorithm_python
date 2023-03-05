import sys
sys.stdin = open('input.txt')


# N은 총 일수, K는 연속하는 일수
N, K = map(int, input().split())
temps = list(map(int, input().split()))

"""
sum을 사용하면 시간초과가 뜬다. 
max_temp = temps[0]
for i in range(0, N-K+1):
    temp = sum(temps[i:i+K])
    max_temp = temp if temp > max_temp else max_temp   
print(max_temp)
"""

sum_temp = [sum(temps[:K])]
i = 1
while i <= N-K:
    temp = sum_temp[i-1] - temps[i-1] + temps[i+K-1]
    sum_temp.append(temp)
    i += 1
print(max(sum_temp))
