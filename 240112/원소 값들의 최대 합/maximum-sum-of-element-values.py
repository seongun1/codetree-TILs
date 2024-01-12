n,m = map(int,input().split())
arr=[0]+ list(map(int,input().split()))

max_ans =0
for i in range(1,n+1):
    ans =0
    a = arr[i]
    for j in range(m):
        ans += a
        a = arr[a]
    max_ans = max(ans,max_ans)

print(max_ans)