# Number of test cases
t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    total_credits = 4 * x + 2 * y
    print(total_credits)
