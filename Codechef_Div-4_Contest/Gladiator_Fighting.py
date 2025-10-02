T = int(input())
for _ in range(T):
    N = int(input())
    min_sum = N - 2
    max_sum = (N - 1) * (N - 2) // 2
    print(min_sum, max_sum)
