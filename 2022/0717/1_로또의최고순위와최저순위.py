def solution(lottos, win_nums):
    answer = []
    check = [0] * 46

    # 1. 내가 고른 로또 번호 체크
    for lotto in lottos:
        check[lotto] += 1
    # 1-1. 실제 로또 번호 체크
    for win_num in win_nums:
        check[win_num] += 1

    least_match = 0
    for i in range(46):
        if i != 0 and check[i] == 2:
            least_match += 1
    # answer.append(least_match)
    most_match = least_match + check[0]

    answer.append(7 - most_match) if most_match > 0 else answer.append(6)
    answer.append(7 - least_match) if least_match > 0 else answer.append(6)

    return answer