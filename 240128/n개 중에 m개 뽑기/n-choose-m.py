n,m = map(int,input().split())

ans = []

def Print():
    for e in ans:
        print(e, end=' ')
    print()


def choose(cnt):
    if cnt == m:
        Print()
        return
    
    for i in range(1,n+1):
        if len(ans)== 0 or ans[-1] < i:
            ans.append(i)
            choose(cnt+1)
            ans.pop()
            
choose(0)