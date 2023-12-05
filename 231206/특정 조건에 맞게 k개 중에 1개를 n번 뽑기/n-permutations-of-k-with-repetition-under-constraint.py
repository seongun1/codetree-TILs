k,n = map(int,input().split())

ans = []
check = []

def println():
    value = ans[1:]
    if value in check:
        return
    check.append(value)
    for s in value:
        print(s, end=' ')
    print()
    

def choose(cur):
    if cur == n+1:
        println()
        return
    
    for i in range(1,k+1):
        if len(ans) <= 2:
            ans.append(i)
            choose(cur+1)
            ans.pop()
        else:
            if ans[-1] == ans[-2] == i:
                continue
            ans.append(i)
            choose(cur+1)
            ans.pop()

    return

choose(0)