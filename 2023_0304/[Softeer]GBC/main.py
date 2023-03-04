import sys

input = sys.stdin.readline

N, M = map(int, input().split())

standard = []

for _ in range(N):
    length, max_velocity = map(int, input().split())
    standard.append((length, max_velocity))

test_array = []
for _ in range(M):
    length, max_velocity = map(int, input().split())
    test_array.append((length, max_velocity))

standard_stack = [standard[0]]
idx = 1
while idx < N:
    a = (standard[idx][0] + standard_stack[idx - 1][0], standard[idx][1])
    standard_stack.append(a)
    idx += 1

test_array_stack = [test_array[0]]
idx = 1
while idx < M:
    a = (test_array[idx][0] + test_array_stack[idx - 1][0], test_array[idx][1])
    test_array_stack.append(a)
    idx += 1

# print(standard_stack)
# print(test_array_stack)

i = j = 0
max_diff = -float('inf')
while i < N or j < M:
    if standard_stack[i][0] < test_array_stack[j][0]:
        diff = test_array_stack[j][1] - standard_stack[i][1]
        if diff > 0 and diff > max_diff:
            max_diff = diff
        i += 1
    elif standard_stack[i][0] > test_array_stack[j][0]:
        diff = test_array_stack[j][1] - standard_stack[i][1]
        if diff > 0 and diff > max_diff:
            max_diff = diff
        j += 1
    else:
        diff = test_array_stack[j][1] - standard_stack[i][1]
        if diff > 0 and diff > max_diff:
            max_diff = diff
        i += 1
        j += 1

if max_diff >= 0:
    print(max_diff)
else:
    print(0)
