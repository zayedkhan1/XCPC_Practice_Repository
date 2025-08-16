
# sorted()--> function sort letters of string alphabitacally and returns a list of characters

# This compares the sorted list of characters from user input with the sorted list of "cat".

# If they are the same, it means the input can be rearranged into "cat"

s=str(input().lower())

if(sorted(s)==sorted('cat')):
    print("Yes")
else:
    print("No")