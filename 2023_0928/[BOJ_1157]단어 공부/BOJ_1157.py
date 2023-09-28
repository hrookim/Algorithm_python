import sys 
sys.stdin = open('input4.txt') 

words = list(input().rstrip())

word_dict = dict()

for apb in words:
    if apb.islower():
        a = apb.upper()
        if word_dict.get(a):
            word_dict[a] += 1
        else:
            word_dict[a] = 1
    else:
        if word_dict.get(apb):
            word_dict[apb] += 1
        else:
            word_dict[apb] = 1

max_num = 0
max_apb = []
for k, v in word_dict.items():
    if v > max_num:
        max_apb = [k]
        max_num = v
    elif v == max_num:
        max_apb.append(k)

# print(word_dict)
if len(max_apb) >= 2:
    print("?")
else:
    print(max_apb[0])