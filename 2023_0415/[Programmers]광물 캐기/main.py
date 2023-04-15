def solution(picks, minerals):
    """
    picks: 갖고 있는 곡괭이의 개수를 나타내는 정수 배열, 총 곡괭이는 최소 1개 이상
    minerals: 광물들의 순서를 나타내는 문자열 배열
    return: 최소한의 피로도
    """
    tiredness = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }
    answer = float("inf")
    # 0. recursive dfs로 곡괭이 순열 만들기
    def perm(curr=0):
        nonlocal answer
        """
        curr: 재귀 깊이
        """
        # 0-1. 다 뽑은 경우 최소 피로도 찾기
        if r == curr:
            tmp = 0
            for i, mineral in enumerate(minerals):
                if i // 5 + 1 > len(test) or tmp >= answer:
                    break
                tmp += tiredness[mineral][test[i // 5]]
            if tmp < answer:
                answer = tmp
            return
        # 0-2. 재귀로 찾아서 들어가기
        for i in range(3):
            if cnt[i] < picks[i]:
                test[curr] = i
                cnt[i] += 1
                perm(curr + 1)
                cnt[i] -= 1

    # dfs 실행
    total_pick = sum(picks)
    if total_pick * 5 > len(minerals):
        r = len(minerals) // 5 + 1
        test = [-1] * r
        cnt = [0] * 3
        perm()
    # 0-2. 곡괭이가 작거나 같은 경우는 가지고 있는 것으로 다 순열 만듦
    else:
        r = total_pick
        test = [-1] * r
        cnt = [0] * 3
        perm()

    return answer


picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
solution(picks, minerals)