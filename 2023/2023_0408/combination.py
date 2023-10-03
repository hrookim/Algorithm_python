def comb(idx, start):
    """
    :param idx: tmp[i]를 채울 i
    :param start: 선택구간의 시작점
    :return: 없음
    """
    global cnt, tmp
    cnt += 1  
    
    if idx == r:
        combinations.append(tmp[:])
    else:
        end = N - r + idx
        for i in range(start, end+1):
            tmp[idx] = numbers[i]
            comb(idx+1, i+1)


numbers = ["A", "B", "C", "D", "E"]
N = len(numbers)
r = 3
tmp = [0] * r
cnt = 0
combinations = []


comb(0, 0)

print(combinations)
