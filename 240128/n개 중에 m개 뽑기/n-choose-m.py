n,m = map(int,input().split())

ans = []

def Print():
    for e in ans:
        print(e, end=' ')
    print()


def choose(idx, cnt):
    if idx == n+1:
        if cnt == m:
            Print()
        return
    
    ans.append(idx)
    choose(idx + 1, cnt+1)
    ans.pop()
    choose(idx + 1, cnt)
            
choose(1,0)