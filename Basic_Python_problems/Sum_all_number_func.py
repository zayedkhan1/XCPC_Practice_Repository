def sum(x):
    y=0
    for i in x:
        y=y+i
    print(y)
numbers_list=list(map(int,input().split()))
sum(numbers_list)