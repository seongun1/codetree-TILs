import sys

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

visited = [[False] * m for _ in range(n)]

def can_go(x,y,h,w):
    for i in range(x,x+h):
        for j in range(y,y+w):
            if not in_range(i,j):
                return False
            if visited[i][j]:
                return False
    return True

def otherBox():
    max_val = -sys.maxsize
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            
            for h in range(1,n+1):
                for w in range(1,m+1):
                    sum_val = 0

                    if not can_go(i,j,h,w):
                        continue

                    for x in range(i,i+h):
                        for y in range(j,j+w):
                            sum_val += arr[x][y]
                    
                    max_val = max(max_val, sum_val)
    return max_val

ans = -sys.maxsize
for i in range(n):
    for j in range(m):
        for h in range(1,n+1):
            for w in range(1,m+1):

                if not can_go(i,j,h,w):
                    continue
                
                sum_val = 0

                for x in range(i,i+h):
                    for y in range(j,j+w):
                        sum_val += arr[x][y]
                        visited[x][y] = True

                ans = max(ans, sum_val + otherBox())

                for x in range(i,i+h):
                    for y in range(j,j+w):
                        visited[x][y] = False
print(ans)