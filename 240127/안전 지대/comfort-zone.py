import sys
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs,dys = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m
    
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

max_safe_cnt = [] # (영역크기, k) 저장

def can_go(x,y,k):
    if not in_range(x,y):
        return False
    
    if visited[x][y] == True or arr[x][y] <= k:
        return False
    
    return True

def dfs(x,y,k):
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        if can_go(next_x,next_y,k):
            visited[next_x][next_y] = True
            dfs(next_x,next_y,k)

for k in range(1,101):
    res = 0

    visited = [
       [False for _ in range(m)]
        for _ in range(n)
    ]

    for x in range(n):
        for y in range(m):
            if can_go(x,y,k):
                visited[x][y] = True
                res += 1
                dfs(x,y,k)
    
    max_safe_cnt.append((res,k))
max_safe_cnt.sort(key = lambda x : (-x[0], x[1]))
print(max_safe_cnt[0][1], max_safe_cnt[0][0])

# def dfs(x,y,k):
#     if not in_range(x,y):
#         return False

#     if visited[x][y]:
#         return False
    
#     if arr[x][y] > k:
#         visited[x][y] = True

#         for dx, dy in zip(dxs, dys):
#             next_x, next_y = x + dx , y + dy

#             dfs(next_x,next_y,k)

#         return True
#     return False


# for k in range(1,101):
#     res = 0

#     visited = [
#        [False for _ in range(m)]
#         for _ in range(n)
#     ]

#     for x in range(n):
#         for y in range(m):
#             if can_go(x,y,k):
#                 visited[x][y] = True
#                 res += 1
#                 dfs(x,y,k)
    
#     max_safe_cnt.append((res,k))
# print(max_safe_cnt)