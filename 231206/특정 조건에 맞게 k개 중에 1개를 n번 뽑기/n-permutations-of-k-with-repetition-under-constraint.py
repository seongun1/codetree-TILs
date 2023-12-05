k,n = map(int,input().split())

ans = []
check = []

def println():
    for e in ans:
        print(e,end=' ')
    print()

def choose(cur):
    if cur == n:
        println()
        return
    
    for i in range(1,k+1):
        if len(ans) < 2:
            ans.append(i)
            choose(cur+1)
            ans.pop()
        else:
            if (ans[-1] != i or ans[-1] != ans[-2]):
                ans.append(i)
                choose(cur+1)
                ans.pop()

    return

choose(0)