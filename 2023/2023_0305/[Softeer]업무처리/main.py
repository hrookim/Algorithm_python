import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


# 전날 받은 거, 혹은 내가 가지고 있는 것에서 처리한 후 위로 올림, 오름차순
def go_out(day):
    global work_tree, H, work_from_left, work_from_right

    idx = 1
    while idx < len(work_tree):
        q = idx // 2
        # 말단이 아닌 경우
        if idx < 2 ** H:
            if day % 2 == 0:
                if idx % 2 == 0 and len(work_from_right[idx]) > 0:
                    work_from_left[q].append(work_from_right[idx][0])
                elif idx % 2 == 1 and len(work_from_right[idx]) > 0:
                    work_from_right[q].append(work_from_right[idx][0])
                work_from_right[idx] = work_from_right[idx][1:]

            else:
                if idx % 2 == 0 and len(work_from_left[idx]) > 0:
                    work_from_left[q].append(work_from_left[idx][0])
                elif idx % 2 == 1 and len(work_from_left[idx]) > 0:
                    work_from_right[q].append(work_from_left[idx][0])
                work_from_left[idx] = work_from_left[idx][1:]


        # 말단인 경우
        else:
            if idx % 2 == 0 and len(work_tree[idx]) > 0:
                work_from_left[q].append(work_tree[idx][0])
            elif idx % 2 == 1 and len(work_tree[idx]) > 0:
                work_from_right[q].append(work_tree[idx][0])
            
            work_tree[idx] = work_tree[idx][1:]

        idx += 1


# . 조직도의 높이, 말단에 대기하는 업무의 개수, 업무가 진행되는 날짜의 수
H, K, R = map(int, input().split())

work_tree = [[] for _ in range(2 ** (H + 1))]
work_from_left = [[] for _ in range(2 ** (H + 1))]
work_from_right = [[] for _ in range(2 ** (H + 1))]

number_leaf_node = 2 ** H

# 말단 직원의 대기 업무
for node in range(2 ** H, 2 ** H + number_leaf_node):
    work_tree[node] = list(map(int, input().split()))

for d in range(1, R+1):
    go_out(d)

print(sum(work_from_left[0]) + sum(work_from_right[0]))