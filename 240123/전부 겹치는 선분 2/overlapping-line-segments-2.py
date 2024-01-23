n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
import sys
def is_possible(i,n):
    max_x1 = 0
    min_x2 = sys.maxsize
    for j in range(n):
        if i==j:
            continue
        x1,x2 = arr[j]
        max_x1 = max(x1,max_x1)
        min_x2 = min(x2,min_x2)
    if min_x2  >= max_x1:
        return True
    else:
        return False
flag = False
for i in range(n):
    if is_possible(i,n):
        print("Yes")
        sys.exit()
print("No")