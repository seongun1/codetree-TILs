m,d = map(int,input().split())
def is_date(m,n):
    if not m>=1 and not m<=12:
        return False
    if m == 1 or m==3 or m==5 or m==7 or m==8 or m==10 or m ==12:
        if 1<= n <= 31:
            return True
        else:
            return False
    elif m==2:
        if 1<=n<=28:
            return True
        else:
            return False
    else:
        if 1<=n<=30:
            return True
        else:
            return False
if is_date(m,d):
    print("Yes")
else:
    print('No')