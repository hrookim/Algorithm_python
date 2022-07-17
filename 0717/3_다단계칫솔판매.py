def solution(enroll, referral, seller, amount):
    answer = []

    # 1. 다단계 형태
    tree = dict()  # 자식 : 부모 형태
    # 2. 판매 형태
    sell = dict()
    sell["minho"] = 0

    i = 0
    while i < len(enroll):
        if referral[i] == "-":
            tree[enroll[i]] = "minho"
        else:
            tree[enroll[i]] = referral[i]
        sell[enroll[i]] = 0
        i += 1

    # 3. 수익 계산하기    
    i = 0
    while i < len(seller):
        price = amount[i] * 100
        c = seller[i]
        p = tree[c]

        while price >= 1:
            to_p = price // 10
            sell[c] += price - to_p

            if p == "minho":
                sell[p] += to_p
                break

            c = p
            p = tree[c]
            price = to_p

        i += 1

    for e in enroll:
        answer.append(sell[e])

    return answer