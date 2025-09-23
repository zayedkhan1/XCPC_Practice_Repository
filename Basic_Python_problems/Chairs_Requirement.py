t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if(x>y):
        res=abs(x-y)
    elif(x<y):
        res=0
    else:
        res=0
    print(res)