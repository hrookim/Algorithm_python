import sys, itertools
sys.stdin = open('input.txt')


def get_subset_sum(B, heights):
    result = []
    for i in range(1, N+1):
        subsets = list(map(sum, list(itertools.combinations(heights, i))))
        for subset in subsets:
            if subset == B:
                return [B]
            elif subset > B:
                result.append(subset)
    return result


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    
    min_diff = 10000000
    total_heights = get_subset_sum(B, heights)
    
    for total_height in total_heights:
        if total_height - B < min_diff:
            min_diff = total_height - B
    
    print(f'#{tc} {min_diff}')