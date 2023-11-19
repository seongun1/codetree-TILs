a,b= map(int,input().split())
def change_num(a,b):
    if a>b:
        a *=2
        b +=10
    else:
        b*=2
        a+=10
    return a,b
a,b = change_num(a,b)
print(a,b)