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
min_perfo = sorted(performances)[0] + 1
price = result = 0
while price <= B:
    for k in perfo_dict.keys():
        if k < min_perfo:
            price += perfo_dict[k] * (min_perfo - k)**2

    if price <= B:
        result = min_perfo
        price = 0
    elif price > B:
        break
    min_perfo += 1


print(result)