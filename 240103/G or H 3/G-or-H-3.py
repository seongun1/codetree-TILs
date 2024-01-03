n,k = map(int,input().split())
arr=['0'] * 10000
for _ in range(n):
    a,b = input().split()
    arr[int(a)] = b
ans =0
for i in range(1,n-k+2):
    tmp=0
    for j in range(i,i+k+1):
        if arr[j] == 'G':
            tmp += 1
        elif arr[j] =='H':
            tmp +=2
    ans = max(tmp,ans)
print(ans)