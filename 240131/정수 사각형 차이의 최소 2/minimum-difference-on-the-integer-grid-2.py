n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def min_init():
    d[0][0] = arr[0][0]

    for i in range(1,n):
        d[0][i] = max(d[0][i-1], arr[0][i])
        d[i][0] = max(d[i-1][0], arr[i][0])

def max_init():
    d[0][0] = arr[0][0]

    for i in range(1,n):
        d[0][i] = min(d[0][i-1], arr[0][i])
        d[i][0] = min(d[i-1][0], arr[i][0])

min_init()

for i in range(1,n):
    for j in range(1,n):
        d[i][j] = max(min(d[i-1][j], d[i][j-1]), arr[i][j])

min_val = d[n-1][n-1]

d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

max_init()

for i in range(1,n):
    for j in range(1,n):
        d[i][j] = min(max(d[i-1][j], d[i][j-1]), arr[i][j])

max_val = d[n-1][n-1]

print(abs(max_val - min_val))