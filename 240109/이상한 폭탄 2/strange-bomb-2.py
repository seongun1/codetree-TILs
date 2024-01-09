n,k = map(int,input().split())
arr=[int(input()) for _ in range(n)]

bomb=[]
for i in range(n):
    a = arr[i]
    for j in range(i+1,n):
        if a == arr[j]:
            if j - i <= k:
                bomb.append(a)
                
print(-1) if not bomb else print(max(bomb))