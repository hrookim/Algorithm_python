import sys
sys.stdin = open("input3.txt")

N, M = map(int, input().split())

_list = []
def perm_recur():
    if len(_list) == M:
        print(*_list)
        return
    for i in range(1, N+1):
        if i not in _list:
            _list.append(i)
            perm_recur()
            _list.pop()

perm_recur()