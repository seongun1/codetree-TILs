import sys

min_val = sys.maxsize

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited =  [False for _ in range(n)]

ans = list()
ans.append(0)
visited[0] = True

def choose(cnt):
    global min_val

    if cnt == n:
        tot = 0
        for i in range(n-1):
            cost = arr[ans[i]][ans[i+1]]

            if cost == 0:
                return
        
            tot += cost
        
        addition = arr[ans[-1]][0]
        if addition == 0:
            return
        
        min_val = min(min_val, tot + addition)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(cnt+1)

            ans.pop()
            visited[i] = False


choose(1)
print(min_val)