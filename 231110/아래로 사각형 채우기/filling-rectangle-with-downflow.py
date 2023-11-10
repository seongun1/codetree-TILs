n=int(input())
arr= [[0 for i in range(n)]for _ in range(n)]
cnt =1
for i in range(n):
    for j in range(n):
        arr[j][i] = cnt
        cnt +=1
for a in arr:
    for i in a:
        print(i,end=' ')
    print()