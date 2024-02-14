import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = -1

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y,h,w):
    for i in range(x,x+h):
        for j in range(y,y+w):
            if not in_range(i,j):
                return False
            if arr[i][j] <= 0:
                return False
    return True

for i in range(n):
    for j in range(m):
        for h in range(1,n+1):
            for w in range(1,m+1):
                if not can_go(i,j,h,w):
                    continue
                
                sum_val = 0

                for x in range(i,i+h):
                    for y in range(j,j+w):
                        sum_val += 1
                

                ans = max(sum_val, ans)
print(ans)