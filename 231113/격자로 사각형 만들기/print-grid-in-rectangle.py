n=int(input())
arr= [[1 for i in range(n)] for i in range(n)]
for i in range(1,n):
    for j in range(1,n):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1]
for a in arr:
    for i in a:
        print(i,end=' ')
    print()