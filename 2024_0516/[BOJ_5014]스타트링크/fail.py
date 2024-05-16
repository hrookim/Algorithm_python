import sys 
sys.stdin = open('input2.txt') 


def solve(diff):
    if diff > 0:
        if U == 0:
            print("use the stairs")
            return
        else:
            if diff % U == 0:
                cnt_U = diff // U
                print(cnt_U)
                return
            else:
                cnt_U = diff // U + 1

            diff_down = S + cnt_U * U - G
            if diff_down % D == 0:
                cnt_D = diff_down // D

                # 검증 과정
                check = min(cnt_U, cnt_D)

                if S + (cnt_U - check) * U + check * (U - D) - (cnt_D - check) * D == G:
                    print(cnt_U + cnt_D)
                    return
            else:
                print("use the stairs")
                return

    else:
        if D == 0:
            print("use the stairs")
            return
        else:
            if abs(diff) % D == 0:
                cnt_D = abs(diff) // D
                print(cnt_D)
                return
            else:
                cnt_D = abs(diff) // D + 1

            diff_up = G - (S - cnt_D * D)
            if diff_up % U == 0:
                cnt_U = diff_up // U

                # 검증 과정
                check = min(cnt_U, cnt_D)

                if S + (cnt_U - check) * U + check * (U - D) - (cnt_D - check) * D == G:
                    print(cnt_U + cnt_D)
                    return
            else:
                print("use the stairs")
                return

# F층으로 이뤄진 고층 건물, 
# 스타트링크가 있는 곳 G층
# 강호는 지금 S층 -> G로 이동해야 함 (엘베)
# 엘베는 버튼 2개 뿐, U층 만큼 up, D층 만큼 down
# G층 도착을 위해 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램! (최소)
# 못 가면 use the stairs 출력

F, S, G, U, D = map(int, input().split())

diff = G - S

cnt_U = 0
cnt_D = 0

solve(diff)