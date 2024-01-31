n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

d = [
    [0 for i in range(n)]
    for _ in range(n)
]

def init():
    d[0][n-1] = arr[0][n-1]

    for i in range(n-2, -1,-1):  
        d[0][i] = d[0][i+1] + arr[0][i]
    
    for i in range(1,n):
        d[i][n-1] = d[i-1][n-1] + arr[i][n-1]
init()

for i in range(1,n):
    for j in range(n-2,-1,-1):
        d[i][j] = min(d[i-1][j], d[i][j+1]) + arr[i][j]
        # print(min(d[i-1][j], d[i][j-1]), d[i-1][j], d[i][j+1] )
        # print("i: {},j: {},arr[i][j]:{} ,d[i][j] : {}".format(i,j,arr[i][j],d[i][j]))

#print(d)
print(d[n-1][0])