import sys

n,m = map(int,input().split())

INT_MIN = -sys.maxsize

d = [
    [ 1 for _ in range(m)]
    for _ in range(n)
]

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def initialize():
    for i in range(n):
        for j in range(n):
            d[i][j] = INT_MIN
    d[0][0] = 1

initialize()

for i in range(1,n):
    for j in range(1,m):
        for x in range(i):
            for y in range(j):
                if d[x][y] == INT_MIN:
                    continue


                if arr[i][j] > arr[x][y]:
                    d[i][j] = max(d[i][j], d[x][y] + 1)
                else:
                    continue

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, d[i][j])
print(ans)