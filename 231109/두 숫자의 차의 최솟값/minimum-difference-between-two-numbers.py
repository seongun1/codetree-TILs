n=int(input())
arr= list(map(int,input().split()))
ans = 100
for i in range(n-1,0,-1):
    if ans > arr[i] - arr[i-1]:
        ans = arr[i] - arr[i-1]
print(ans)