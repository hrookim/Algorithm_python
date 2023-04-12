import sys 
# sys.stdin = open('input1.txt') 

# 종말의 수: 6이 적어도 3개 이상 연속으로 들어가는 수
# 666 -> 1666 -> 2666 -> 3666
# N번째 영화의 제목은 N번째로 작은 종말의 수


# N <= 10000
N = int(input())

"""
666 -> 1666 -> 2666 -> 3666 -> 4666 -> 5666
-> 6661 ~ 6669 -> 
"""

cnt = 0
base = 665
while cnt < N:
    base += 1
    if "666" in str(base):
        cnt += 1

print(base)
    
        