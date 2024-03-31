import sys
sys.stdin = open("input5.txt")
from collections import deque


def move_people():
    global N, M, people_distance, exit_ij, maze, total_moves

    m = 0
    while m < len(people_distance):
        pi, pj = people_distance.popleft()
        pdist = abs(pi - exit_ij[0]) + abs(pj - exit_ij[1])

        # 이동 가능한 칸 구하기
        possible_ni, possible_nj = 0, 0
        possible_ndist = pdist
        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:  # 상하 이동이 우선시
            ni, nj = pi + di, pj + dj
            ndist = abs(ni - exit_ij[0]) + abs(nj - exit_ij[1])
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0 and ndist < possible_ndist:
                possible_ndist = ndist
                possible_ni, possible_nj = ni, nj

        if (possible_ni, possible_nj) == (0, 0) and possible_ndist == pdist:
            m += 1
            people_distance.append([pi, pj])
            continue
        # 그 칸이 출구라면 멈추기
        if [possible_ni, possible_nj] == exit_ij:
            total_moves += 1
            continue

        # 그 칸이 벽이 아니라면 이동하기
        if maze[possible_ni][possible_nj] == 0:
            total_moves += 1
            m += 1
            people_distance.append([possible_ni, possible_nj])
        # 벽이라면 그냥 가만히 있기
        else:
            m += 1
            people_distance.append([pi, pj])


def find_square():
    global N, exit_ij, people_distance
    ei, ej = exit_ij
    min_len = 11
    min_i, min_j = 11, 11
    for pi, pj in people_distance:
        r, c = abs(ei - pi), abs(ej - pj)
        curr_len = max(r, c)

        if curr_len <= min_len:

            # r==c인 경우, 그 자체로 정사각형의 대각전 꼭지점이 됨
            if r == c == curr_len:
                i_start, j_start = min(ei, pi), min(ej, pj)
                if curr_len < min_len or (i_start, j_start) < (min_i, min_j):
                    min_len = curr_len
                    min_i, min_j = i_start, j_start

            # r이 정사각형 길이인 경우
            elif curr_len == r:
                i_start = min(ei, pi)
                for poss_j_start in range(0, N - curr_len):
                    if poss_j_start <= ej <= poss_j_start + curr_len and poss_j_start <= pj <= poss_j_start + curr_len:
                        if curr_len < min_len or (i_start, poss_j_start) < (min_i, min_j):
                            min_len = curr_len
                            min_i, min_j = i_start, poss_j_start
                            break
            # c가 정사각형 길이인 경우
            elif curr_len == c:
                j_start = min(ej, pj)
                for poss_i_start in range(0, N - curr_len):
                    if poss_i_start <= ei <= poss_i_start + curr_len and poss_i_start <= pi <= poss_i_start + curr_len:
                        if curr_len < min_len or (poss_i_start, j_start) < (min_i, min_j):
                            min_len = curr_len
                            min_i, min_j = poss_i_start, j_start
                            break

    return (min_i, min_j, min_len)


def rotate(r, c, slen):
    global N, maze, exit_ij, people_distance
    S = slen+1

    new_maze = [[[] for _ in range(slen + 1)] for _ in range(slen + 1)]
    small_maze = [[0] * (slen + 1) for _ in range(slen + 1)]
    # 1) 일부 구역을 small_maze에 복사해놓기
    for i in range(r, r + S):
        for j in range(c, c + S):
            # 1-1)출구표시
            if [i, j] == exit_ij:
                small_maze[i - r][j - c] = 999
            else:
                small_maze[i - r][j - c] = maze[i][j]

    # 2) small_maze에서 new_maze로 복사
    for i in range(S):
        for j in range(S):
            new_maze[j][slen - i] = (small_maze[i][j], i + r, j + c)

    # 3) new_maze에서 원래 maze로 값 복사
    for i in range(r, r + S):
        for j in range(c, c + S):
            if new_maze[i - r][j - c][0] == 999:
                exit_ij = [i, j]
                maze[i][j] = 0
            elif new_maze[i - r][j - c][0] > 0:
                maze[i][j] = new_maze[i - r][j - c][0] - 1
            else:
                maze[i][j] = 0

    # 3-1) 변경되어야 할 사람들 수정
    for m in range(len(people_distance)):
        pi, pj = people_distance[m][0], people_distance[m][1]

        for i in range(S):
            for j in range(S):
                if new_maze[i][j][1] == pi and new_maze[i][j][2] == pj:
                    people_distance[m][0] = i + r
                    people_distance[m][1] = j + c
                    break


# Input
N, M, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
people = [list(map(int, input().split())) for _ in range(M)]
exit_ij = list(map(int, input().split()))
exit_ij = [exit_ij[0] - 1, exit_ij[1] - 1]  # (0, 0) 시작인 것으로 조정

# Add-on
people_distance = deque([])  # [[i, j, dist]]
total_moves = 0

for pi, pj in people:
    # (0, 0) 시작인 것으로 조정
    people_distance.append([pi - 1, pj - 1])

for _ in range(K):
    move_people()
    if not people_distance:
        break
    sr, sc, slen = find_square()
    rotate(sr, sc, slen)

print(total_moves)
print(exit_ij[0] + 1, exit_ij[1] + 1)  # 원래대로 +1 조정