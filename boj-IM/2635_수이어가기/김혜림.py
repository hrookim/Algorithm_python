import sys
sys.stdin = open('input.txt')


def find_maxlen_seq(N):
    max_len = 1
    ans = []
    
    # 두번째 수가 무엇일까? 규칙을 적용한 수열이 길어지려면, 두번째 수가 N의 반보다 커야 한다.
    search_arr = list(range(N//2, N+1))
    for num in search_arr:
        seq = [N, num]
        while seq[-1] >= 0:
            seq.append(seq[-2] - seq[-1])
        else:
            if len(seq)-1 > max_len:
                max_len = len(seq)-1
                ans = seq[:-1]
    
    return max_len, *ans


N = int(input())
result = find_maxlen_seq(N)
print(result[0])
print(*result[1:])