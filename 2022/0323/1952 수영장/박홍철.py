import sys
sys.stdin = open("input.txt")


def cal_rest_month_fee(idx_month, current_fee):
    if idx_month >= 12:
        return current_fee
    if idx_month == 10:
        if months[10] + months[11] > fees[2]:
            return current_fee + fees[2]
        else:
            return current_fee + months[10] + months[11]
    if idx_month == 11:
        if months[11] > fees[2]:
            return current_fee + fees[2]
        else:
            return current_fee + months[11]

    if months[idx_month] + months[idx_month+1] + months[idx_month+2] > fees[2]:
        return min(cal_rest_month_fee(idx_month+3, current_fee + fees[2]), cal_rest_month_fee(idx_month+1, current_fee + months[idx_month]))
    else:
        return cal_rest_month_fee(idx_month+1, current_fee + months[idx_month])


T = int(input())

for tc in range(1, T+1):
    fees = list(map(int, input().split()))
    months = list(map(int, input().split()))
    for i in range(12):
        months[i] = fees[1] if fees[1] < months[i] * fees[0] else months[i] * fees[0]

    result = min(fees[3], cal_rest_month_fee(0, 0))

    print(f'#{tc} {result}')


