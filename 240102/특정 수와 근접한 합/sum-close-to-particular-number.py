n,s =map(int,input().split())
arr=list(map(int,input().split()))
ans =999
for i in range(n):
    for j in range(i+1,n):
        if ans > abs(sum(arr) - (arr[i] + arr[j]) - s):
            ans = abs(sum(arr) - (arr[i] + arr[j]) - s)
print(ans)