
x, y = map(int, input().split())
perimeter = 2 * (x + y)

if perimeter >= 1000:
    print("YES")
else:
    print("NO")
