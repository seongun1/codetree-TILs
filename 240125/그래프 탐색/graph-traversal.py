import sys
n,m = map(int,input().split())

arr = []
for i in range(m):
    s,e = map(int,input().split())
    arr.append((s,e))

start = [i[0] for i in arr]
end = [i[1] for i in arr]

visited = [False for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

#  양 방향
for s,e in zip(start, end):
    graph[s].append(e)
    graph[e].append(s)

# for s,e in arr:
#     graph[s].append(e)
#     graph[e].append(s)

cnt = 0
def dfs(vertex):
    global cnt
    for cur in graph[vertex]:
        #print(cur)
        if not visited[cur]:
            visited[cur] = True
            cnt += 1
            dfs(cur)

vertex = 1
visited[vertex] = True
dfs(vertex)

print(cnt)