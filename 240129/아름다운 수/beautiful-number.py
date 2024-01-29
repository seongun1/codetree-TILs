n = int(input())

ans = []
count = 0

def possible():
    idx = 0

    while idx < n:
        if ans[idx] + idx -1 >= n:
            return False

        for i in range(idx, ans[idx] + idx):
            if ans[i] != ans[idx]:
                return False
        
        idx += ans[idx]
    return True
            
        

def choose(cnt):
    global count
    
    if cnt == n:
        if possible():
            count += 1
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cnt+1)
        ans.pop()

choose(0)
print(count)