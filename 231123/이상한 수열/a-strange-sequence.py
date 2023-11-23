n=int(input())
def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fun(int(n/3)) + fun(n-1)
print(fun(n))