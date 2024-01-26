n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global cnt

    if not in_range(x,y):
        return False

    if arr[x][y] == 1:
        arr[x][y] = 2
        cnt += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False

res = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i,j):
            res += 1
            ans.append(cnt)

print(res)
ans.sort()
for i in ans:
    print(i)