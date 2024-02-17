n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(m)
]

graph = [
    [] for _ in range(n+1)
]

s,e = list(), list()
cnt = 0

for i in range(m):
    s.append(arr[i][0])
    e.append(arr[i][1])

for start, end in zip(s,e):
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (n+1)

def dfs(v):
    global cnt

    for cur_v in graph[v]:
        if not visited[cur_v]:
            visited[cur_v] = True
            cnt += 1
            dfs(cur_v)

visited[1] = True
dfs(1)
print(cnt)