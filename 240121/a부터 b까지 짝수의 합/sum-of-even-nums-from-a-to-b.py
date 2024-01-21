a,b = map(int,input().split())
ans =0
for i in range(a,b+1):
    if not i%2:
        ans +=i
print(ans)