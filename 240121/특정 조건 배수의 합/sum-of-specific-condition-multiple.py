a,b = map(int,input().split())
ans =0
a,b = min(a,b),max(a,b)
for i in range(a,b+1):
    if not i%5:
        ans +=i
print(ans)