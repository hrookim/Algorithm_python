from itertools import combinations
import sys

sys.stdin = open("input2.txt")

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def calculate(graph):
    global N
    group_dict = dict()
    
    visited = [[0] * N for _ in range(N)]
    number = 0  # 그룹의 번호
    
    # 1-1. 구역 구해서, 그룹 정보 딕셔너리 완성 + 그래프 변경하기
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                number += 1
                color_number = graph[i][j]
                total_number = 0
                
                visited[i][j] = 1
                stack = [(i, j)]
                while stack:
                    ci, cj = stack.pop()
                    graph[ci][cj] = number
                    total_number += 1
                    
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = ci+di, cj+dj
                        if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] == color_number and not visited[ni][nj]:
                            stack.append((ni, nj))
                            visited[ni][nj] = 1
                
                else:
                    group_dict[number] = {
                        "color": color_number,
                        "total": total_number,
                        "start": (i, j)
                    }
        
    # 1-2. 인접 두 쌍 구해서 예술점수 구하기
    score = 0
    L = len(group_dict) 
    for a, b in combinations(range(1, L+1), 2):
        ab_adjacent = 0
        a_si, a_sj = group_dict[a]["start"]
        a_color = group_dict[a]["color"]
        a_total = group_dict[a]["total"]
        
        b_color = group_dict[b]["color"]
        b_total = group_dict[b]["total"]
        
        visited = dict()
        visited[(a_si, a_sj)] = 1
        stack = [(a_si, a_sj)]
        while stack:
            ci, cj = stack.pop()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if graph[ni][nj] == a and not visited.get((ni, nj)):
                        stack.append((ni, nj))
                        visited[(ni, nj)] = 1
                    elif graph[ni][nj] == b and not visited.get((ni, nj)):
                        ab_adjacent += 1
                        visited[(ni, nj)] = [(ci, cj)]
                    elif graph[ni][nj] == b and visited.get((ni, nj)):
                        if (ci, cj) not in visited[(ni, nj)]:
                            ab_adjacent += 1
                            visited[(ni, nj)].append((ci, cj))
        
        else:
            score += (a_total + b_total) * a_color * b_color * ab_adjacent
            # print(a, b, "조합", ab_adjacent)
    return score


def rotate(graph):
    global N
    middle = N//2
    new_graph = [[0] * N for _ in range(N)]
    
    # 2-1. 반시계 90도 회전
    for p in range(N):
        new_graph[N-1-middle][p] = graph[p][middle]
        new_graph[N-1-p][middle] = graph[middle][p]
    
    # 2-2. 시계 90도 회전
    for i in range(middle):
        for j in range(middle):
            new_graph[j][middle-1-i] = graph[i][j]
    
    for i in range(middle):
        for j in range(middle+1, N):
            new_graph[j-middle-1][N-1-i] = graph[i][j]

    for i in range(middle+1, N):
        for j in range(middle):
            new_graph[j+middle+1][N-1-i] = graph[i][j]

    for i in range(middle+1, N):
        for j in range(middle+1, N):
            new_graph[j][N+middle-i] = graph[i][j]

    return new_graph


spin_1_graph = rotate(graph)
spin_2_graph = rotate(spin_1_graph)
spin_3_graph = rotate(spin_2_graph)

result = calculate(graph)
result += calculate(spin_1_graph)
result += calculate(spin_2_graph)
result += calculate(spin_3_graph)
print(result)