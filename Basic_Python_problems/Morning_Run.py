# Read input values
x, y = map(int, input().split())

# Calculate perimeter
perimeter = 2 * (x + y)

# Check if Chef's goal is met
if perimeter >= 1000:
    print("YES")
else:
    print("NO")
