n,k =map(int,input().split())
arr=list(map(int,input().split()))
def is_possible(max_num):
    tmp=[]
    for i in range(n):
        if arr[i] <= max_num:
            tmp.append(i)
    if 0 not in tmp or n-1 not in tmp:
        return False
    for j in range(len(tmp) -1):
        if tmp[j+1] - tmp[j] >k:
            return False
    
    return True

for i in range(1,101):
    if is_possible(i):
        print(i)
        break