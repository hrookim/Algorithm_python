import sys 
sys.stdin = open('input3.txt') 

"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""

N, M = map(int, input().split())

# nPr 구하기
def permutation(start, r):
    global results, numbers
    
    if start == r:
        results.append(numbers[:r])
    else:
        for i in range(start, N):
            numbers[start], numbers[i] = numbers[i], numbers[start]
            permutation(start+1, r)
            numbers[i], numbers[start] = numbers[start], numbers[i]
  
    
results = []
numbers = list(range(1, N + 1))
permutation(0, M)
for res in sorted(results):
    print(*res)

