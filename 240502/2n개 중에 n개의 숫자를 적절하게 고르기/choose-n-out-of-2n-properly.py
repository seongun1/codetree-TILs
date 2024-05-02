import sys

n = int(input())
arr = list(map(int,input().split()))

box = list()

min_val = sys.maxsize

def choose(idx, cnt):
    global min_val

    if cnt == n:
        min_val = min(min_val, abs(sum(arr) - 2 * sum(box)))
        return

    if idx == 2 * n:
        return
    
    box.append(arr[idx])
    choose(idx+1, cnt+1)
    box.pop()
    choose(idx+1, cnt)

choose(0,0)
print(min_val)