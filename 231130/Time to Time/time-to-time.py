a,b,c,d =map(int,input().split())

def how_much(a,b,c,d):
    cnt =0
    while (1):
        if a==c and b==d:
            break
        if b ==60:
            a +=1
            b=0
        b+=1
        cnt +=1
    return cnt
print (how_much(a,b,c,d))