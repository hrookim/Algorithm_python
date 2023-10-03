import sys
sys.stdin = open("input1.txt")
# input = sys.stdin.readline

plain_text = list(input().rstrip())
key_text = list(input().rstrip())

# 0. 플레이페어 키 어레이 만들기
# 0-1. 중복확인용 딕셔너리
key_dict = {}
key_coordinate = {}  # 좌표값을 적어주기 위한 용
for ascii in range(65, 65 + 26):
    if ascii == 74:
        continue
    key_dict[chr(ascii)] = 0

# 0-2. 키 어레이 초반 작업
key_array = [[0] * 5 for _ in range(5)]

idx = 0
for i in range(5):
    for j in range(5):
        while key_array[i][j] == 0 and idx < len(key_text):
            alphabet = key_text[idx]
            if key_dict.get(alphabet) == 0:
                key_array[i][j] = alphabet
                key_dict.pop(alphabet)
                key_coordinate[alphabet] = (i, j)
                idx += 1
            elif not key_dict.get(alphabet):
                idx += 1

# 0-2. 키 어레이 완성
idx = 0
key_dict_keys = list(key_dict.keys())
for i in range(5):
    for j in range(5):
        if key_array[i][j] == 0:
            key_array[i][j] = key_dict_keys[idx]
            key_coordinate[key_dict_keys[idx]] = (i, j)
            idx += 1

# 1. 문자열 쪼개서 쌍 이루기
idx = 0
plain_set = []
while idx < len(plain_text):
    if idx % 2:
        if plain_text[idx] == plain_text[idx - 1]:
            if plain_text[idx] == "X":
                plain_text = plain_text[:idx] + ["Q"] + plain_text[idx:]
            else:
                plain_text = plain_text[:idx] + ["X"] + plain_text[idx:]

        else:
            plain_set.append((plain_text[idx - 1], plain_text[idx]))
            idx += 1
    else:
        if idx == len(plain_text) - 1:
            plain_set.append((plain_text[idx], "X"))
            break
        idx += 1

# 2. 문자 암호화하기
result = []
for a1, a2 in plain_set:
    a1_i, a1_j = key_coordinate[a1]
    a2_i, a2_j = key_coordinate[a2]

    # 2-1. 행이 같은 경우
    if a1_i == a2_i:
        replaced_a1, replaced_a2 = key_array[a1_i][(a1_j + 1) % 5], key_array[a2_i][(a2_j + 1) % 5]
        result += [replaced_a1, replaced_a2]

    # 2-2. 열이 같은 경우
    elif a1_j == a2_j:
        replaced_a1, replaced_a2 = key_array[(a1_i + 1) % 5][a1_j], key_array[(a2_i + 1) % 5][a2_j]
        result += [replaced_a1, replaced_a2]
    # 2-3. 행 열이 다 다른 경우
    else:
        replaced_a1, replaced_a2 = key_array[a1_i][a2_j], key_array[a2_i][a1_j]
        result += [replaced_a1, replaced_a2]

print("".join(result))