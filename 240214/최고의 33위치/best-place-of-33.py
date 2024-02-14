import sys
n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def getSize(x,y):
    size = 0

    for i in range(x,x+3):
        for j in range(y,y+3):
            if arr[i][j]:
                size += 1

    return size

max_val = -sys.maxsize
for x in range(n):
    for y in range(n):
        if x + 2 >= n:
            continue
        if y + 2 >= n:
            continue
        
        tmp_val = getSize(x,y)

        max_val = max(max_val, tmp_val)

print(max_val)