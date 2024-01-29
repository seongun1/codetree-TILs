import sys
from collections import deque

n = int(input())
x1,y1,x2,y2 = tuple(map(int,input().split()))

dxs,dys = [-1,-2,-2,-1,1,2,2,1], [-2,-1,1,2,2,1,-1,-2]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

q = deque()
q.append((x1-1, y1-1))

def bfs():
    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy

            if can_go(next_x,next_y):
                visited[next_x][next_y] = visited[x][y] + 1
                q.append((next_x,next_y))

bfs()
if visited[x2-1][y2-1] == 0:
    print(-1)
else:
    print(visited[x2-1][y2-1])