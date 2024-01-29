import sys

n = int(input())
ans = []
max_val = -sys.maxsize

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [False for _ in range(n)]

def calc():
    val = 0
    for e in ans:
        val += e
    return val

def choose(cnt):
    global max_val

    if cnt == n:
        #print(ans)
        max_val = max(max_val, calc())
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            
            ans.append(arr[i][cnt])
            choose(cnt+1)
            ans.pop()
            
            visited[i] = False

choose(0)
print(max_val)