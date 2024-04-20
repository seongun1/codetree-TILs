n = int(input())

ans = []
max_val = 0

def beauty():

    idx = 0
    while idx < n:

        if idx + ans[idx] - 1 >= n:
            return False

        for i in range(idx, idx + ans[idx]):
            if ans[i] != ans[idx]:
                return False
        
        idx += ans[idx]
    
    return True

def choose(cnt):
    global max_val

    if cnt == n:
        if beauty():
            max_val +=1
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cnt+1)
        ans.pop()

choose(0)
print(max_val)