import sys
sys.stdin = open("input.txt")


def DFS(left_change, cards):
    global len_cards, max_card, visited
    # 0. 종료조건
    if left_change <= 0:
        tmp = int("".join(cards))
        if tmp > max_card:
            max_card = tmp
        return
    
    # 1. 완전탐색
    for i in range(len_cards):
        for j in range(i+1, len_cards):
            cards[i], cards[j] = cards[j], cards[i]
            tmp = "".join(cards) + str(left_change)
            if not visited.get(tmp):
                visited[tmp] = 1
                DFS(left_change - 1, cards)
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    
    cards = list(a)
    len_cards = len(cards)
    change = int(b)
    
    max_card = 0
    visited = {}
    DFS(change, cards)
    print(f'#{tc} {max_card}')
