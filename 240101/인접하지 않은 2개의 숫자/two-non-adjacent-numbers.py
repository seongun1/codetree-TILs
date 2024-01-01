n=int(input())
arr=list(map(int,input().split()))
ans =0
for i in range(n):
    for j in range(i+2,n):
        if ans < arr[i] + arr[j]:
            ans = arr[i]+arr[j]
print(ans)