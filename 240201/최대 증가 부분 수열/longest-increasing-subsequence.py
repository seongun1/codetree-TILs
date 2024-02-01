n = int(input())
arr = list(map(int,input().split()))

d = [1 for _ in range(n+1)]

for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[j] + 1, d[i])
print(max(d))