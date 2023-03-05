import sys 
sys.stdin = open('input1.txt') 


def DFS(i, j, l):
    global arr, max_len, visited
    asc = ord(arr[i][j]) - 65
    
    # 0. 백트랙킹, 이미 방문한적이 있다면
    if visited[asc]:
        if l > max_len:
            max_len = l
        return
    
    # 1. 이동, 방문한적이 없다면
    visited[asc] = True
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= i+di < R and 0 <= j+dj < C:
            DFS(i+di, j+dj, l+1)
    visited[asc] = False


R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

max_len = 0
visited = [False] * 26
DFS(0, 0, 0)
print(max_len)