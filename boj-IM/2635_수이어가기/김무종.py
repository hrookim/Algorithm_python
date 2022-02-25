import sys
sys.stdin = open('input.txt')

def get_num(num):
    list1 = [T, num]
    global num_list
    n = 3
    while list1[n-3] - list1[n-2] >= 0:
        list1.append(list1[n-3]-list1[n-2])
        n = n+1
    num_list.append(list1)


T = int(input())
choice = [i for i in range(1, T+1)]
final_list = []
num_list = []
for num in choice:
    final_list.append(get_num(num))
max_set1 = len(num_list[0])
max_idx = 0
for idx, set1 in enumerate(num_list):
    if len(set1) > max_set1:
        max_set1 = len(set1)
        max_idx = idx
print(max_set1)
print(' '.join(map(str, num_list[max_idx])))

