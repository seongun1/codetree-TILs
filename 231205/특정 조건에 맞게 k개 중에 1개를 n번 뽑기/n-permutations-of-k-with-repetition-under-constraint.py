k,n = map(int,input().split())

ans = []
check = []

def println():
    string = ''
    for i in ans[1:]:
        string += str(i)
    if string not in check:
        check.append(string)
        for s in string:
            print(s, end=' ')
        print()
    else:
        return
        
    
    

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