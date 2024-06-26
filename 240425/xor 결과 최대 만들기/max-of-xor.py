n,m = map(int,input().split())
arr = list(map(int,input().split()))
max_val = 0

ans = []

def Print():
    val = ans[0]
    if len(ans) >= 2:
        for i in ans[1:]:
            val ^= i
    return val

def choose(idx, cnt):
    global max_val

    if cnt == m:
        max_val = max(max_val, Print())
        return

    if idx == n:
        return
    
    ans.append(arr[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)

choose(0,0)
print(max_val)