n,m = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

cnt =1

for t in range(m+n-1):
    for i in range(n):
        for j in range(m):
            if (t == i+j):
                arr[i][j] = cnt
                cnt +=1
for a in arr:
    for i in a:
        print(i,end=' ')
    print()