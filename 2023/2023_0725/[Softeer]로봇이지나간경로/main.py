import sys

input = sys.stdin.readline

# L: 왼쪽으로 90도 회전, 바라보는 방향 변경
# R: 오른쪽으로 90도 회전, 바라보는 방향 변경
# A: 바라보는 방향으로 2칸 전진 / 격자판 바깥을 나간다면 명령 수행 X

# 로봇이 같은 칸을 두번 이상 방문하지 X

# 처음 로봇을 어떤칸, 방향에 둬야 하는가?
# 어떤 명령어를 순서대로 입력해야 하는가?
# 명령어의 수를 최소화하게 만들어야 한다

# 목표를 달성할 수 있는 방안이 여러개 가능, 아무거나 답 가능


didj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dict_dir = {
    (0, 1): 1,
    (1, 0): 2,
    (0, -1): 3,
    (-1, 0): 4
}


def is_possible_sp(i, j):
    global I, J, routes
    connection = 0
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < I and 0 <= nj < J and routes[ni][nj] == "#":
            connection += 1

    if connection > 1:
        return False
    else:
        return True


def find_cmd(i, j):
    global I, J, routes, didj, dict_dir
    start_cd, cmd = 0, ""

    visited = [[0] * J for _ in range(I)]
    to_visit = [(i, j)]
    cd = 0
    while to_visit:
        ci, cj = to_visit.pop()
        visited[ci][cj] = 1
        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < I and 0 <= nj < J and routes[ni][nj] == "#" and not visited[ni][nj]:
                visited[ni][nj] = 1
                # 방향 체크 코드
                if (ci, cj) == (i, j):
                    cd = dict_dir[(di, dj)]
                    start_cd = cd
                else:
                    nd = dict_dir[(di, dj)]
                    dd = nd - cd
                    if dd in (1, -3):
                        cmd += "R"
                    elif dd in (-1, 3):
                        cmd += "L"
                    cd = nd  # 추가한 버전

                to_visit.append((ci + 2 * di, cj + 2 * dj))
                cmd += "A"
    return (cmd, start_cd)


I, J = map(int, input().split())

routes = [list(input().rstrip()) for _ in range(I)]

dirr = ["", ">", "v", "<", "^"]

min_cmd = "A" * 1000
min_cd = ""
min_st = (0, 0)
for i in range(I):
    for j in range(J):
        if routes[i][j] == "#" and is_possible_sp(i, j):
            cmd, start_cd = find_cmd(i, j)
            if len(cmd) < len(min_cmd):
                min_st = (i, j)
                min_cd = dirr[start_cd]
                min_cmd = cmd

print(min_st[0] + 1, min_st[1] + 1)
print(min_cd)
print(min_cmd)