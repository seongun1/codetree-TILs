n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 북 남 서 동
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(x,y,direct):

    time = 1

    while in_range(x,y):

        if arr[x][y] == 1:
            direct = 3 - direct
        elif arr[x][y] == 2:
            direct = (direct + 2)  % 4

        x,y = x + dx[direct], y + dy[direct]
        time += 1

    return time

max_val = 0
for i in range(n):
    max_val = max(max_val, move(0,i,1))
    max_val = max(max_val, move(i,0,3))
    max_val = max(max_val, move(n-1,i,0))
    max_val = max(max_val, move(i,n-1,2))
print(max_val)