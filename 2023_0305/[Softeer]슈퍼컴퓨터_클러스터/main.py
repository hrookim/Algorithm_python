import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, B = map(int, input().split())
performances = list(map(int, input().split()))

perfo_dict = {}
for p in performances:
    if not perfo_dict.get(p):
        perfo_dict[p] = 1
    else:
        perfo_dict[p] += 1


#. 최저 성능 컴퓨터의 최댓값 찾기
result = 0
left, right = sorted(performances)[0]+1,  10**10
while left <= right:
    price = 0
    mid = (left + right) // 2
    
    for k in perfo_dict.keys():
        if k < mid:
            price += perfo_dict[k] * (mid - k)**2
    
    if price == B:
        result = mid
        break
    if price < B:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
        
        