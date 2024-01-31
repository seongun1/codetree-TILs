import sys

ans = sys.maxsize
n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def init():
    for i in range(n):
        for j in range(n):
            d[i][j] = sys.maxsize

    d[0][0] = arr[0][0]

    for i in range(1,n):
        d[i][0] = max(d[i-1][0] , arr[i][0])
    for i in range(1,n):
        d[0][i] = max(d[0][i-1] , arr[0][i])

def sol(lower):
    for i in range(n):
        for j in range(n):
            if lower > arr[i][j]:
                arr[i][j] = sys.maxsize
    
    init()

    for i in range(1,n):
        for j in range(1,n):
            d[i][j] = max(min(d[i-1][j], d[i][j-1]), arr[i][j])
    
    return d[n-1][n-1]

for lower in range(1,101):
    upper = sol(lower)

    if upper == sys.maxsize:
        continue

    ans = min(ans, upper - lower)
print(ans)