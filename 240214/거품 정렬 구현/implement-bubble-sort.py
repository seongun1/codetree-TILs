n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(n-1):
        if arr[i] < arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
for a in arr:
    print(a,end=' ')