t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    c.sort(reverse=True)
    result=sum(c[:k])
    print(result)