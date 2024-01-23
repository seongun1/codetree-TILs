n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr=[]
ans =0
for i in range(n-1):
    if a[i] > b[i]:
        diff = a[i] - b[i]
        ans += diff
        a[i] -= diff
        a[i+1] += diff
    elif a[i] < b[i]:
        diff = b[i] - a[i]
        a[i] += diff
        a[i-1] -= diff
print(ans)