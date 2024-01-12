n,m = map(int,input().split())
arr=[0]*(n+1)
tmp = list(map(int,input().split()))
for i in range(1,n+1):
    arr[i] = tmp[i-1]
max_ans =0
for i in range(1,n+1):
    ans =0
    a = arr[i]
    ans +=a
    for j in range(m-1):
        b= arr[a]
        arr[a] = a
        ans += b
        a=b
    
    max_ans = max(ans,max_ans)

    for k in range(1,n+1):
        arr[k] = tmp[k-1]

print(max_ans)