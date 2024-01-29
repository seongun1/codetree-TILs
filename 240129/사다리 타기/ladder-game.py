import sys

n,m = map(int,input().split())

arr = []
for i in range(m):
    a,b = map(int,input().split())
    arr.append((b, a-1))

arr.sort()

ans = []

min_val = sys.maxsize

def calc():
    num1 = [i for i in range(n)]
    num2 = [i for i in range(n)]

    for _ , idx in ans:
        num1[idx], num1[idx+1] = num1[idx+1], num1[idx]
    for _ , idx in arr:
        num1[idx], num1[idx+1] = num1[idx+1], num1[idx]
    
    for i in range(n):
        if num1[i] != num2[i]:
            return False
    return True
    

def choose(idx, cnt):
    global min_val

    if cnt == m:
        if calc():
            min_val = min(min_val, len(ans))
        return
    
    if idx == m:
        return

    ans.append(arr[idx])
    choose(idx+1, cnt+1)
    ans.pop()
    choose(idx+1, cnt+1)
    
choose(0,0)
print(min_val)