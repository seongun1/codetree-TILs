n,m = map(int,input().split())

d = [
    [ 1 for _ in range(m)]
    for _ in range(n)
]

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i in range(1,n):
    for j in range(1,n):
        for x in range(i):
            for y in range(i):
                if arr[i][j] > arr[x][y]:
                    d[i][j] = max(d[i][j], d[x][y] + 1)

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, d[i][j])
print(ans)