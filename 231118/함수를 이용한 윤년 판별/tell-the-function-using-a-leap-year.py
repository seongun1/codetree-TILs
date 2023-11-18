y=int(input())
def is_yunyear(n):
    if not n%4 and not n%100 and not n%400:
        return True
    elif not n%4 and not n%100:
        return False
    elif not n%4:
        return True
    return False
if is_yunyear(y):
    print('true')
else:
    print('false')