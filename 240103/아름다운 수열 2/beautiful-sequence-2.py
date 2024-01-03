n,m =map(int,input().split())
a=list(map(int,input().split()))
b = list(map(int,input().split()))
ans =0
for i in range(n-m+1):
    cnt =0
    for j in range(i,i+m):
        if a[j] in b:
            cnt +=1
        else:
            break
        if cnt ==m:
            ans +=1
print(ans)