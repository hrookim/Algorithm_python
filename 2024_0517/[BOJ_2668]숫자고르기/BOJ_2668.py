import sys 
sys.stdin = open('input1.txt') 

N = int(input())

matrix = [[n for n in range(0, N+1)]]

row = [0]
for _ in range(N):
    number = int(input())
    row.append(number)
matrix.append(row)

def find_circle(idx):
    global N, matrix
    
    visited = [[0, 0] for _ in range(N+1)]
    
    # 1. 이동하기 
    to_visit = [idx]     # 현재 idx와 그것이 첫번째 row인지 두번째 row인지
    while to_visit:
        cidx = to_visit.pop()
        visited[cidx][0] = 1

        nidx = matrix[1][cidx]
        
        if not visited[nidx][1]:
            visited[nidx][1] = 1
            to_visit.append(nidx)
        else:
            break
        
    # 2. 순환인지 체크하기
    result = list()
    for i in range(1, N+1):
        if sum(visited[i]) == 1:
            return False
        elif sum(visited[i]) == 2:
            result.append(i)
    return result
            

result_set = list()
for idx in range(N+1):
    if idx != 0:
        res = find_circle(idx)
        if res:
            result_set += res

fin = sorted((set(result_set)))
l = len(fin)
print(l)
for i in range(l):
    print(fin[i])

            
            

