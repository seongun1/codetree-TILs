a = input()
b = input()

n,m = len(a), len(b)

d = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

path =[
    [(0,0) for _ in range(m+1)]
    for _ in range(n+1)
]

for i in range(1,n+1):
    for j in range(1,m+1):
        if d[i][j] < d[i-1][j]:
            d[i][j] = d[i-1][j]
            path[i][j] = (i-1, j)

        if d[i][j] < d[i][j-1]:
            d[i][j] = d[i][j-1]
            path[i][j] = (i, j-1)
        
        if a[i-1] == b[j-1] and d[i][j] < d[i-1][j-1] + 1:
            d[i][j] = d[i-1][j-1] + 1
            path[i][j] = (i-1, j-1)

lcs = []
while n > 0 and m > 0:
    if path[n][m] == (n-1, m-1) and a[n-1] == b[m-1]:
        lcs.append(a[n-1])
        n -= 1
        m -= 1
    else:
        n,m = path[n][m]

print(''.join(reversed(lcs)))