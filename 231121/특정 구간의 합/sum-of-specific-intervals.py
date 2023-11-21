n,m = map(int,input().split())
arr = list(map(int,input().split()))

def sum_val(a,b):
    tmp =0
    for i in range(a-1,b):
        tmp += arr[i]
    return tmp
    
for i in range(m):
    a,b=map(int,input().split())
    print(sum_val(a,b))