r, b = map(int, input().split())
g = min(r, b)  
res = 5*g + (r-g)*1 + (b-g)*2
print(res)
