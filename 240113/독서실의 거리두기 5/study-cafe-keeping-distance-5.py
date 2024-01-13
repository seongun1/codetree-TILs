n=int(input())
tmp = str(input())
tmp = list(tmp)
arr= list(map(int,tmp))

ans = 0
for i in range(n):
    if arr[i] == 0:
        arr[i] = 1
        dist = n
        for j in range(n):
            for k in range(j+1,n):
                if arr[j] == 1 and arr[k] ==1:
                    dist = min(k-j,dist)
        ans = max(dist,ans)
        arr[i] = 0
print(ans)