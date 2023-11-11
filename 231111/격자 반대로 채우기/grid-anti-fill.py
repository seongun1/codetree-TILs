n=int(input())
arr= [[0 for _ in range(n)] for _ in range(n)]
cnt = 1
if n%2:
    for i in range(n-1,-1,-1):
        if not i %2:
            for j in range(n-1,-1,-1):
                arr[j][i] = cnt
                cnt +=1
        else:
            for j in range(n):
                arr[j][i] = cnt
                cnt +=1
else:
    for i in range(n-1,-1,-1):
        if i %2:
            for j in range(n-1,-1,-1):
                arr[j][i] = cnt
                cnt +=1
        else:
            for j in range(n):
                arr[j][i] = cnt
                cnt +=1
    

for a in arr:
    for i in a:
        print(i,end=' ')
    print()