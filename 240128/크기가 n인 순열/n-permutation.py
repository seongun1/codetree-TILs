n = int(input())

visited = [False for _ in range(n+1)]

def Print():
    for e in ans:
        print(e,end=' ')
    print()

ans = []

def choose(cnt):
    if cnt == n+1:
        Print()
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True  
            ans.append(i)

            choose(cnt+1)

            ans.pop()
            visited[i] = False
choose(1)