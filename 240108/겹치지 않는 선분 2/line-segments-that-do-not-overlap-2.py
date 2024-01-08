n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

cnt = [True] * (n+1)
cnt[0] = False
for i in range(n):
    for j in range(i+1,n):
        x1,x2 = arr[i]
        x3,x4 = arr[j]
        if x1 < x2 and x3 < x4:
            if x3 < x1 < x2 < x4 or x1<x3 <x4 <x2:
                cnt[i] = False
                cnt[j] = False
ans=0
for t in cnt:
    if t == True:
        ans +=1
print(ans)