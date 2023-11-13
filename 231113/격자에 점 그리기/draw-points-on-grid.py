n,m = map(int,input().split())
arr= [[0 for i in range(n)] for i in range(n)]
cnt =1
for i in range(m):
    x,y= map(int,input().split())
    arr[x-1][y-1] = cnt
    cnt +=1
for a in arr:
    for i in a:
        print(i,end=' ')
    print()