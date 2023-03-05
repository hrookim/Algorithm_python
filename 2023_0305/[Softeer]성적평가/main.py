import sys
input = sys.stdin.readline


#. 각 점수별 등수를 찾는 함수
def find_rank_by_score(scores):
    sorted_scores = sorted(scores, reverse=True)
    ranks = {}

    idx, current_rank = 0, 1
    while idx < len(scores):
        current_score = sorted_scores[idx]
        if not ranks.get(current_score):
            ranks[current_score] = current_rank
        current_rank += 1
        idx += 1
    return ranks


#. 참가자의 수
N = int(input())

#. 대회별 참가자의 점수
first_contest = list(map(int, input().split()))
second_contest = list(map(int, input().split()))
third_contest = list(map(int, input().split()))
final_score = [first_contest[idx] + second_contest[idx] + third_contest[idx] for idx in range(N)]


first_rank_by_score = find_rank_by_score(first_contest)
second_rank_by_score = find_rank_by_score(second_contest)
third_rank_by_score = find_rank_by_score(third_contest)
final_rank_by_score = find_rank_by_score(final_score)


first_rank = [first_rank_by_score[first_contest[idx]] for idx in range(N)]
second_rank = [second_rank_by_score[second_contest[idx]] for idx in range(N)]
third_rank = [third_rank_by_score[third_contest[idx]] for idx in range(N)]
final_rank = [final_rank_by_score[final_score[idx]] for idx in range(N)]

print(*first_rank)
print(*second_rank)
print(*third_rank)
print(*final_rank)