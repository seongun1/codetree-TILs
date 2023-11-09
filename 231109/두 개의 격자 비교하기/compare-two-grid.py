n,m = map(int,input().split())
arr1 = [list(map(int,input().split()))for i in range(4)]
arr2 = [list(map(int,input().split()))for i in range(4)]
arr3 = [[1 for _ in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            arr3[i][j] = 0
for a in arr3:
    for i in a:
        print(i,end=' ')
    print()