n=int(input())
arr=list(map(int,input().split()))
max_sum =0
ans =0
for i in range(n):
    for j in range(n):
        if abs(i-j) <=1:
            continue
        max_sum = max(arr[i]+arr[j],max_sum)
    ans = max(ans,max_sum)
print(ans)