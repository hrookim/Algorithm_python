def solution(picks, minerals):
    tiredness = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }
    answer = float("inf")
    
    def perm(curr=0):
        nonlocal answer
        if r == curr:
            tmp = 0
            for i, mineral in enumerate(minerals):
                if i // 5 + 1 > len(test) or tmp >= answer:
                    break
                tmp += tiredness[mineral][test[i // 5]]
            if tmp < answer:
                answer = tmp
            return
        
        for i in range(3):
            if cnt[i] < picks[i]:
                test[curr] = i
                cnt[i] += 1
                perm(curr + 1)
                cnt[i] -= 1

    total_pick = sum(picks)
    if total_pick * 5 > len(minerals):
        r = len(minerals) // 5 + 1
        test = [-1] * r
        cnt = [0] * 3
        perm()
    else:
        r = total_pick
        test = [-1] * r
        cnt = [0] * 3
        perm()

    return answer


picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
solution(picks, minerals)