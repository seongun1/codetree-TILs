n,m,k = map(int,input().split())

arr = list(map(int,input().split()))
ans = [1] * k

max_val = 0

def calc():
    global max_val
    val = 0

    for i in ans:
        if i >= m:
            val += 1
    max_val = max(max_val, val)

def choose(idx):

    if idx == n:
        calc()
        return
    
    for i in range(k):
        ans[i] += arr[idx]
        choose(idx+1)
        ans[i] -= arr[idx]

    calc()
    return

choose(0)
print(max_val)