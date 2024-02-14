import sys

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = -sys.maxsize

def square(x,y):
    size, min_val = 0, sys.maxsize

    for i in range(x,x+2):
        for j in range(y,y+2):
            size += arr[i][j]
            min_val = min(min_val, arr[i][j])
    
    return size - min_val

def line(x,y):
    size, size2 = 0, 0

    for i in range(3):
        if y + i >= m:
            size = 0
            break
        size += arr[x][y+i]

    for i in range(3):
        if x + i >= n:
            size2 = 0
            break
        size2 += arr[x+i][y]

    return max(size, size2)
    

for x in range(n):
    for y in range(m):
        if x + 1 >= n or y + 1 >= m:
            continue
        max_val = max(max_val, square(x,y))

for x in range(n):
    for y in range(m):
        if x + 2 >= n and y + 2 >= m:
            continue
        
        max_val = max(max_val, line(x,y))
print(max_val)