n=int(input())
def star(n):
    if n==0:
        return
    for i in range(n):
        print('*',end=' ')
    print()
    star(n-1)
    for i in range(n):
        print('*',end=' ')
    print()
star(n)