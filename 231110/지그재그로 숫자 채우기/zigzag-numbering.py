n,m = map(int,input().split())
cnt =0
arr = [[0 for i in range(m)]for _ in range(n)]
for i in range(m):
    if not i%2:
        for j in range(n):
            arr[j][i] = cnt
            cnt +=1
    else:
        for j in range(n-1,-1,-1):
            arr[j][i] = cnt
            cnt +=1
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()