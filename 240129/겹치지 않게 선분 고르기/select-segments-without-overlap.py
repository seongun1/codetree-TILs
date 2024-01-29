import sys

max_val = -sys.maxsize
n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
ans = []
def possible():

    for i, val1 in enumerate(ans):
        for j, val2 in enumerate(ans):
            x1, y1 = val1
            x2, y2 = val2
            
            if i < j:
                if (x1 <= x2 <= y1) or (x1 <= y2 <= y1) or (x2 <= x1 <= y2) or (x2 <= y1 <= y2):
                    return False
    return True


def choose(idx, cnt):
    global max_val

    if cnt == n:
        if possible():
            max_val = max(max_val, len(ans))
        return
    
    if idx == n:
        return

    ans.append(arr[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt+1)
choose(0,0)
print(max_val)