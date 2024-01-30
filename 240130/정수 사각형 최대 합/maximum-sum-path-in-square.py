import sys

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
    d[0][0] = arr[0][0]

    for i in range(1,n):
        d[i][0] = d[i-1][0] + arr[i][0]

    for i in range(1,n):
        d[0][i] = d[0][i-1] + arr[0][i]
    
    # for i in range(1,n):
    #     d[i][i] = d[i-1][i-1] + arr[i][i]

init()

for i in range(1,n):
    for j in range(1,n):
        d[i][j] = max(d[i-1][j], d[i][j-1]) + arr[i][j]
print(d[n-1][n-1])
# ans = -sys.maxsize
# j = 0
# for i in range(n):
#     if ans <= d[n-1][i]:
#         ans = d[n-1][i]
#         j = i
#     #ans = max(ans, d[n-1][i])
# for k in range(j+1,n):
#     ans += arr[n-1][k]

# print(ans)