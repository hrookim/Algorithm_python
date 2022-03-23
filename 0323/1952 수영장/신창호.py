import sys
sys.stdin = open('input.txt')


def func(month, calc):
    global answer

    if calc >= answer:
        return
    if month > 12:
        answer = calc
        return

    if plans[month]:
        # 1일
        func(month + 1, calc + costs[0] * plans[month])
        # 1달
        func(month + 1, calc + costs[1])
        # 3달
        func(month + 3, calc + costs[2])
    else:
        func(month + 1, calc)


T = int(input())
for tc in range(1, T+1):
    costs = list(map(int, input().split()))
    plans = [0] + list(map(int, input().split()))

    answer = costs[-1]
    func(1, 0)
    print(f'#{tc}', answer)
