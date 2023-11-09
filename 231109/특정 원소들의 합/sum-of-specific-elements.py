arr=[list(map(int,input().split()))for i in range(4)]
tmp=0
for i in range(4):
    for j in range(i+1):
        tmp += arr[i][j]
print(tmp)