n = int(input())
arr = list(map(int,input().split()))

d = [
    [1] * 2
    for _ in range(n)
]

for i in range(1,n):
    for j in range(i):

        if arr[i] > arr[j]:
            d[i][0] = max(d[i][0], d[j][0] + 1)

        if arr[i] < arr[j]:
            d[i][1] = max(d[i][1], d[j][1] + 1)

    d[i][1] = max(d[i][1], d[i][0])

ans = 0
for i in range(n):
    for j in range(2):
        ans = max(ans, d[i][j])
print(ans)