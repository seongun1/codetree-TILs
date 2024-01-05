arr=list(map(int,input().split()))
def find_diff(a,b,c):
    num = arr[a]+arr[b]+arr[c]
    return abs(sum(arr) - num -num)
ans =999999
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            ans = min(ans,find_diff(i,j,k))
print(ans)