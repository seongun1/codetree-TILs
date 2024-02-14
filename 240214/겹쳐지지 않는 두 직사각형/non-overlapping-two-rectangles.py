import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = -sys.maxsize

def in_range(x,y):
    return 0<=x<n and 0<=y<m

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def able(x,y,a,b):
    for i in range(x, x+a):
        for j in range(y, y+b):
            if visited[i][j]:
                return False
            if not in_range(i,j):
                return False
    return True

def make():
    max_val = -sys.maxsize
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            for h in range(1,n):
                for w in range(1,m):
                    sum_val = 0

                    if not able(i,j,h,w):
                        continue
                    
                    for x in range(i,i+h):
                        for y in range(j,j+w):
                            sum_val = arr[x][y]
                    
                    max_val = max(max_val, sum_val)
    return max_val

for i in range(n):
    for j in range(m):
        for h in range(1,n):
            for w in range(1,m):
                
                sum_val = 0

                if not able(i,j,h,w):
                    continue
                
                for x in range(i,i+h):
                    for y in range(j,j+w):
                        sum_val = arr[x][y]
                        visited[x][y] = True

                ans = max(ans, sum_val + make())

                for x in range(i,i+h):
                    for y in range(j,j+w):
                        visited[x][y] = False
print(ans)