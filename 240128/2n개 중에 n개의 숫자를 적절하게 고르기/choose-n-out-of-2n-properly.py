import sys

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

min_val = sys.maxsize

def calc():
    return abs((sum(arr) - sum(ans)) - sum(ans))
ans = []
def choose(idx, cnt):
    global min_val

    if cnt == n:
        min_val = min(min_val, calc())
        return
    
    if idx == 2 * n:
        return
    
    ans.append(arr[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt)

choose(0,0)
print(min_val)