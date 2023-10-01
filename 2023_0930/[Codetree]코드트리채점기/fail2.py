import sys
sys.stdin = open("input2.txt")

from queue import PriorityQueue

waiting_q = PriorityQueue()
waiting_url = dict()
total_url = dict()
idx_url = 1
done_domain = dict()
ing_domain = dict()
judges = dict()
min_judge_id = 1
max_judge_id = 0


def prepare(number, url):
    """
    100
    :param number: 채점기의 개수 
    :param url: 초기 task의 url, 바로 대기큐로 들어간다
    """
    global judges, total_url, idx_url, waiting_q, max_judge_id
    max_judge_id = number

    time, priority = 0, 1
    total_url[1] = {
        "time": time,
        "priority": priority,
        "url": url
    }
    waiting_q.put((priority, time, 1))
    idx_url += 1

    waiting_url[url] = 1


def judge_request(time, priority, url):
    """
    200, task가 대기큐에 추가되는 함수
    :param time: 해당 명령이 진행되는 시각
    :param priority: task의 우선순위
    :param url: task의 url
    """
    global total_url, idx_url, waiting_q, waiting_url

    if not waiting_url.get(url):
        total_url[idx_url] = {
            "time": time,
            "priority": priority,
            "url": url
        }
        waiting_q.put((priority, time, idx_url))
        waiting_url[url] = 1
        idx_url += 1


def judge_try(time):
    """
    300, 대기큐에서 우선순위 가장 높은 task를 채점하기 시작
    :param time: 해당 명령이 진행되는 시각
    """
    global waiting_q, waiting_url, total_url, ing_domain, min_judge_id, judges, max_judge_id

    # 3-0. 채점이 아예 불가능한 경우
    if min_judge_id > max_judge_id:
        return

    # 3-1. 채점이 가능한 경우 찾기
    tmp = []
    while waiting_q.qsize() > 0:
        _time, _priority, idx = waiting_q.get()
        url = total_url[idx]["url"]

        # 3-2. 채점 안되는 경우
        domain, _id = url.split("/")
        if ing_domain.get(domain):
            tmp.append((_time, _priority, idx))
            continue

        if done_domain.get(domain):
            if time < done_domain[domain]["start"] + 3 * done_domain[domain]["gap"]:
                tmp.append((_time, _priority, idx))
                continue

        # 3-2. 채점 가능한 경우 채점하기 + 쉬고있는 가장 번호 작은 채점기 갱신
        judges[min_judge_id] = idx
        total_url[idx]["start"] = time
        waiting_url.pop(url)

        if ing_domain.get(domain):
            ing_domain[domain] += 1
        else:
            ing_domain[domain] = 1

        i = min_judge_id
        while judges.get(i):
            i += 1
        else:
            min_judge_id = i

        if tmp:
            for t in tmp:
                waiting_q.put(t)
        break
    else:
        if tmp:
            for t in tmp:
                waiting_q.put(t)


def judge_end(time, number_judge):
    """
    특정 채점기에서 진행되고 있는 채점을 종료한다    
    :param time: 해당 명령이 진행되는 시각
    :param number_judge: 채점기 번호
    """
    global total_url, judges, min_judge_id, done_domain, ing_domain

    # 4-1. 빈 채점기면 그냥 패스
    if not judges.get(number_judge):
        return

    # 4-2. 채점 중이었다면, 채점 종료하기
    idx = judges[number_judge]
    url = total_url[idx]["url"]
    start = total_url[idx]["start"]
    domain, _id = url.split("/")

    done_domain[domain] = {
        "start": start,
        "gap": time - start
    }

    if ing_domain[domain] > 1:
        ing_domain[domain] -= 1
    elif ing_domain[domain] == 1:
        ing_domain.pop(domain)

    # 최소 빈 채점기 갱신
    if number_judge < min_judge_id:
        min_judge_id = number_judge
    judges.pop(number_judge)


def inquire(time):
    """
    해당 시각에 대기큐에 있는 task의 수 출력
    :param time: 해당 명령이 진행되는 시각
    """
    global waiting_q
    print(waiting_q.qsize())


N = int(input())
for _ in range(N):
    commands = list(input().split())

    cmd_no = commands[0]
    if cmd_no == "100":
        prepare(int(commands[1]), commands[-1])
    elif cmd_no == "200":
        judge_request(int(commands[1]), int(commands[2]), commands[-1])
    elif cmd_no == "300":
        judge_try(int(commands[1]))
    elif cmd_no == "400":
        judge_end(int(commands[1]), int(commands[-1]))
    elif cmd_no == "500":
        inquire(int(commands[1]))
