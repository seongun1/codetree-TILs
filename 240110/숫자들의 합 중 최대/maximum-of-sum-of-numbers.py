x,y = map(int,input().split())
ans =0
for i in range(x,y+1):
    tmp=list(str(i))
    a=0
    for t in tmp:
        a += int(t)
    ans = max(a,ans)
print(ans)