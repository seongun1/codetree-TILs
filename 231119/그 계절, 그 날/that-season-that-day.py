y,m,d = map(int,input().split())
def is_yunyear(y):
    if y%4:
        return False
    elif y%100:
        return True
    elif not y%400:
        return True
    return False

def end_of_month(y,m):
    if m==11 or m==9 or m==6 or m==4:
        return 30
    elif m==2:
        if is_yunyear(y):
            return 29
        else:
            return 28
    return 31

def def_season(y,m,d):
    if m == 12 or 1<= m <=2:
        if 1 <= d <= end_of_month(y,m):
            return 'Winter'
        else:
            return '-1'
    elif 3 <= m <= 5:
        if 1 <= d <= end_of_month(y,m):
            return 'Spring'
        else:
            return '-1'
    elif 6<= m <=8:
        if 1 <= d <= end_of_month(y,m):
            return 'Summer'
        else:
            return '-1'
    elif 9<= m <=11:
        if 1 <= d <= end_of_month(y,m):
            return 'Fall'
        else:
            return '-1'
    return '-1'


print(def_season(y,m,d))