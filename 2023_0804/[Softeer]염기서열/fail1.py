# good nt = N
# len(nt) = M
# 초염기서열: 좋은 염기서열의 조건을 만족할 수 있음
# 근데 좋은 염기서열을 모두 만족할 수는 없어서, 여러 초염기서열로 -> 여러 좋은 염기서열을 커버
# 좋은 염기서열을 모두 커버하기 위한 초염기서열의 최소갯수는?

N, M = map(int, input().split())

good_nt_list = [list(input()) for _ in range(N)]
good_nt_list.sort(reverse=True)

visited = [0] * N

result = 0
i = 0
while i < N:

    if not visited[i]:
        visited[i] = 1
        control = good_nt_list[i]
        comparison = []

        # 1. 비교군이 될 수 있는 후보 가져오기
        for j in range(i + 1, len(good_nt_list)):
            test = good_nt_list[j]
            if not visited[j] and test[0] == "." or test[0] == control[0]:
                comparison.append((j, test))

        # 2. 비교해보기
        for comp in comparison:
            is_same_group = True
            for m in range(1, M):
                if comp[1][m] == control[m] or control[m] == "." or comp[1][m] == ".":
                    continue
                else:
                    is_same_group = False
                    break
            if is_same_group:
                visited[comp[0]] = 1

        # 3. 그룹 개수에 추가하고 다음으로 넘어가기
        result += 1
        i += 1
    else:
        i += 1
print(result)