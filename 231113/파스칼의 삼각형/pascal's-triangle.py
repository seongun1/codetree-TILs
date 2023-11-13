n=int(input())
arr= [[1 for j in range(i)] for i in range(1,n+1)]


for i in range(n-1):
    for j in range(i):
        arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
for a in arr:
    for i in a:
        print(i,end=' ')
    print()