import sys
sys.stdin = open("input1.txt")

S = list(input().strip())

CNT_0 = S.count("0") // 2
CNT_1 = S.count("1") // 2

cnt0 = cnt1 = 0

for s in S:
    if s == "0":
        if cnt0 < CNT_0:
            print("0", end="")
            cnt0 += 1
        else:
            continue
    else:
        if cnt1 >= CNT_1:
            print("1", end="")
        else:
            cnt1 += 1