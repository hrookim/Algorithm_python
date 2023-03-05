n = int(input())
INF = float('inf')
numbers = [0, 1] + [INF]*n

for i in range(2, n+1):
    j = 1
    minn = numbers[i]
    while j ** 2 <= i:
        tmp = i - j**2
        minn = min(numbers[tmp], minn)
        j += 1
    numbers[i] = minn+1
print(numbers[n])