n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
max_num =-1
for i in range(n):
    for j in range(n-2):
        max_num = max(max_num,arr[i][j]+arr[i][j+1]+arr[i][j+2])
print(max_num)