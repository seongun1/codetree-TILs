n = int(input())

visited = [False for _ in range(n+1)]

def Print():
    for e in ans:
        print(e,end=' ')
    print()

ans = []

def choose(cnt):
    if cnt == n:
        Print()
        return
    
    for i in range(n, 0, -1): 
        if not visited[i]:
            visited[i] = True
            ans.append(i)

            choose(cnt + 1)

            ans.pop()
            visited[i] = False
choose(0)