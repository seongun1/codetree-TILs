n=int(input())
cnt=0
def fun(n):
    global cnt
    if n==1:
        return cnt
    cnt +=1
    if not n%2:
        return fun(n//2)
    else:
        return fun(3*n +1)
print(fun(n))