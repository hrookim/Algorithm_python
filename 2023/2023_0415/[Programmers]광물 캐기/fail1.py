from itertools import permutations


def solution(picks, minerals):
    """
    picks: 갖고 있는 곡괭이의 개수를 나타내는 정수 배열, 총 곡괭이는 최소 1개 이상
    minerals: 광물들의 순서를 나타내는 문자열 배열
    return: 최소한의 피로도
    """
    tireness = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }

    total_pick = sum(picks)

    # 0. 완전 탐색 모든 경우의 수 만들기
    _list = []
    for i, v in enumerate(picks):
        for _ in range(v):
            _list.append(i)
    # 0-1. 곡괭이가 더 많은 경우는 r개 만큼만 뽑아서 순열 만듦
    if total_pick * 5 > len(minerals):
        r = len(minerals) // 5 + 1
        test_list = permutations(_list, r)
    # 0-2. 곡괭이가 작거나 같은 경우는 가지고 있는 것으로 다 순열 만듦
    else:
        test_list = permutations(_list)

    # 1. 최소 피로도 찾기
    answer = float("inf")
    test_set = set(test_list)
    for test in test_set:
        tmp = 0
        for i, mineral in enumerate(minerals):
            if i // 5 + 1 > len(test) or tmp >= answer:
                break
            tmp += tireness[mineral][test[i // 5]]
        if tmp < answer:
            answer = tmp

    return answer