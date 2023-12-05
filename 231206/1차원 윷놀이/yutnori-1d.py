n,m,k = map(int,input().split())

arr = list(map(int,input().split()))

role = [1] * (k+1)
max_val = 0

def println():
    global max_val
    cnt = 0
    for i in range(1,k+1):
        if role[i] >= m:
            cnt += 1
    max_val = max(max_val, cnt)

def choose(cur):
    if cur == n:
        println()
        return

    for i in range(1,k+1):
        if role[i] >= m:
            continue
        
        role[i] += arr[cur]
        choose(cur+1)
        role[i] -= arr[cur]
    return
choose(0)
print(max_val)