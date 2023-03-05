# N개의 악보 -> 난이도있음 1 ≤ x ≤ y ≤ N 을 만족하는 두 정수 x, y를 골라 x번부터 y번까지의 악보를 번호 순서대로 연주하는 것이 피아노 체조이다.
# 지금 연주하는 악보가 바로 다음에 연주할 악보보다 어렵다면 실수를 한다. 
# 마지막으로 연주하는 y번 악보에선 실수 없음
# 실수하는 곡은 몇곡이나 될지?

import sys 
sys.stdin = open('input2.txt') 
input = sys.stdin.readline
"""input
N: 악보의 개수
1~N까지 악보의 난이도
Q: 질문의 개수
x, y => Q줄에 거쳐 전달
"""

N = int(input())    # 악보의 개수
difficulty = [0] + list(map(int, input().split()))  # 악보 번호별 난도
check = [0] * (N+1)
# 실수할 수 있는 순서를 미리 체크
idx = 1
while idx < N:
    if difficulty[idx]-difficulty[idx+1] > 0:
        check[idx] += 1
    idx += 1

Q = int(input())
for _ in range(Q):
    # 시작 번호 -> 마지막 번호
    x, y = map(int, input().split())

    i = x
    mistakes = 0
    while i < y:
        if check[i]:
            mistakes += 1
        i += 1
    
    print(mistakes)
        
        
        

