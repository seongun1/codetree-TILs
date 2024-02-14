import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def getDist(x,y,h,k):
    cnt = 0
    d = [h,k,h,k]

    for dx, dy, move in zip(dxs, dys, d):
        for _ in range(move):

            x += dx
            y += dy

            if not in_range(x,y):
                return 0
            
            cnt += arr[x][y]
    return cnt

max_val = -sys.maxsize

for i in range(n):
    for j in range(n):
        for a in range(1,n):
            for b in range(1,n):
                max_val = max(max_val, getDist(i,j,a,b))
print(max_val)