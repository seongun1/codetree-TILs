n,k = map(int,input().split())
arr=[int(input()) for _ in range(n)]

tmp = [0 for i in range(n+1)]
existed = [False for _ in range(n+1)]

for i in range(n):
    bomb = arr[i]
    for j in range(i+1,n):
        if bomb == arr[j] and j-i <=k:
            existed[j] = True
            existed[i] = True
for k in range(n):
    if existed[k] == True:
        tmp[arr[k]] +=1
ans =0
count =0
for index,bomb_count in enumerate(tmp):
    if count <= bomb_count and bomb_count !=0 :
        ans = index
        count = bomb_count

print(ans)