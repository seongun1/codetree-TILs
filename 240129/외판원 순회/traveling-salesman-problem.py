import sys

n = int(input())

min_val = -sys.maxsize

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [False for _ in range(n)]

ans = []

def choose(cnt):
    global min_val

    if cnt == n:
        for i in range(n-1):
            cost =  arr[ans[i]][ans[i+1]]

            if cost == 0:
                return
            
            cost += arr[ans[i]][ans[i+1]]
        
        addition = arr[ans[-1]][0]
        if addition == 0:
            return
        
        min_val = min(min_val, cost + addition)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(cnt+1)

            ans.pop()
            visited[i] = False

visited[0]= True
ans.append(0)
choose(1)

print(min_val)