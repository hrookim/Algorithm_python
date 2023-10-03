from collections import deque


def solution(plans):
    answer = []
    changed_plans = []
    for plan in plans:
        _list = list(map(int, plan[1].split(":")))
        start_time = _list[0] * 60 + _list[1]
        changed_plans.append([plan[0], start_time, int(plan[2])])

    changed_plans.sort(key=lambda x: x[1])
    print(changed_plans)

    l = len(plans)
    to_do = deque([])
    for i in range(l):
        # 뒷 과제가 있다면,
        if i < l - 1:
            current_end = changed_plans[i][1] + changed_plans[i][2]
            next_start = changed_plans[i + 1][1]
            # 시작+소요 <= 뒷과제 시작이면 과제 마무리 할 수 있다.
            if current_end <= next_start:
                answer.append(changed_plans[i][0])

                # 그런데 시간도 남았고 todo가 있다면, 
                while next_start - current_end > 0 and to_do:
                    name, s, r = to_do.pop()
                    # 현재시간+소요시간 <= 다음시작시간 인 경우만 들어옴 
                    if current_end + r <= next_start:
                        answer.append(name)
                        current_end += r
                    # 그렇지 않으면, 다시 to_do로 들어감
                    else:
                        to_do.append([name, s, current_end + r - next_start])
                        break
            # 과제를 마무리하지 못하면, 남은시간을 가지고 to_do에 저장한다.
            else:
                changed_plans[i][2] = current_end - next_start
                to_do.append(changed_plans[i])
        # 마지막 과제이면        
        else:
            answer.append(changed_plans[i][0])

    # 마지막 과제까지 끝냈는데도 to_do가 남아있으면
    while to_do:
        name, s, r = to_do.pop()
        answer.append(name)
    return answer