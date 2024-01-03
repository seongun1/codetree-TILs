n,k = map(int,input().split())
arr=['0'] * 10001
for _ in range(n):
    a,b = input().split()
    arr[int(a)] = b
ans =0
for i in range(1,10001-k):
    tmp=0
    for j in range(i,i+k+1):
        if arr[j] == 'G':
            tmp += 1
        elif arr[j] =='H':
            tmp +=2
    ans = max(tmp,ans)
print(ans)