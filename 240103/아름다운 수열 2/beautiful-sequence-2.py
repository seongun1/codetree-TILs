n,m =map(int,input().split())
a=list(map(int,input().split()))
b = list(map(int,input().split()))
exits=[True] * m
ans =0
for i in range(n-m+1):
    cnt =0
    for j in range(i,i+m):
        for k in range(m):
            if a[j] == b[k] and exits[k] == True:
                cnt +=1
                exits[k] =False
    if cnt == m:
        ans +=1

    exits=[True] * m
        

print(ans)