"""
어떤 두 자리의 위치를 변경해서 해당하는 전체 경우의 수를 찾는다면,
완전탐색을 생각해볼 수 있다.
"""

def DFS(left_cnt, cards):
    global len_cards
    # 0. 종료조건
    if left_cnt <= 0:
        return
    # 1. 완전탐색
    for i in range(len_cards):
        for j in range(i + 1, len_cards):
            cards[i], cards[j] = cards[j], cards[i]
            DFS(left_cnt - 1, cards)
            cards[i], cards[j] = cards[j], cards[i]

