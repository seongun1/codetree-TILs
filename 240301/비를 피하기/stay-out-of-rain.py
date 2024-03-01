from collections import deque
import sys

n,h,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# arr의 2로부터 3까지의 거리를 2의 자리에 표시
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

ppl = list()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ppl.append((i,j))

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n
        
def bfs():
    while q:
        x,y,val = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] != 1:
                visited[nx][ny] = True 
                
                if arr[nx][ny] != 3: 
                    q.append((nx, ny, val + 1))
                
                elif arr[nx][ny] == 3: 
                    return val + 1 

    return -1

for p in ppl:
    x,y = p

    q = deque([(x,y,0)])
    
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    visited[x][y] = True

    temp[x][y] = bfs()

for i in temp:
    print(*i)