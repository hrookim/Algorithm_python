import sys
sys.stdin = open('input1.txt') 

# 총 블록 수
# 블록별 장애물 수 (한줄에 하나씩 출력, 오름차순)

N = int(input())

graph = [list(map(int, list(input()))) for _ in range(N)]

number_block = 0
list_block = []

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 0. 장애물 블록 시작점을 확인
        if graph[i][j] and not visited[i][j]:
            number_block += 1
            if number_block != len(list_block):
                list_block.append(0)

            # 1. 그래프 탐색
            to_visit = [(i, j)]
            visited[i][j] = 1
            while to_visit:
                ci, cj = to_visit.pop()
                list_block[-1] += 1

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni = ci + di
                    nj = cj + dj
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and graph[ni][nj]:
                        visited[ni][nj] = 1
                        to_visit.append((ni, nj))

print(number_block)
for n in sorted(list_block):
    print(n)
