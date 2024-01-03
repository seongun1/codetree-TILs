n,k =map(int,input().split())
arr=list(map(int,input().split()))
ans = 0
for i in range(n-k+1):
    tmp =0 
    for j in range(i,i+k):
        tmp += arr[j]
    ans = max(tmp,ans)
print(ans)