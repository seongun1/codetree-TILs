n=int(input())
arr=list(map(int,input().split()))
result = []
for i in range(n):
    result.append(arr[i])
    if not i%2:
        result.sort()
        print(result[int(i/2)],end=' ')