a,b,c= map(int,input().split())


def is_when(a,b,c):
    if a<= 11 and b<=11and c<11:
        return -1
    cnt =0
    d,h,m =11,11,11
    while (1):
        if d == a and h == b and m ==c:
            break
        cnt +=1
        m +=1
        if m ==60:
            h +=1
            m=0
        if h == 24:
            d +=1
            h=0
    return cnt
print(is_when(a,b,c))