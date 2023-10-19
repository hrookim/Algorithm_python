"""
최소의 마법의 돌을 사용하여 층수 이동하기
엘리베이터를 타고 0층으로 내려간다
"""


def solution(storey):
    answer = 0

    Q = storey

    while Q >= 1:
        R = Q % 10
        Q = Q // 10

        if R < 5:
            answer += R
        elif R > 5:
            answer += 10 - R
            Q += 1
        elif R == 5:
            answer += 5
            if Q % 10 >= 5:
                Q += 1

    else:
        answer += Q

    return answer