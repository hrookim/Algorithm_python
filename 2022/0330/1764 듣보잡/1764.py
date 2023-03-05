import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

unheards = set([input() for _ in range(N)])
unseens = set([input() for _ in range(M)])

ans_lst = sorted(list(unheards & unseens))

print(len(ans_lst))
for ans in ans_lst:
    print(ans)