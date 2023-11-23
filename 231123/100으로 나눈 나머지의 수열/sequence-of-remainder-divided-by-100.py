n=int(input())
def fun(n):
    if n==1:
        return 2
    elif n==2:
        return 4
    else:
        return (fun(n-2) * fun(n-1)) %100 
print(fun(n))