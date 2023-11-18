a,b=map(int,input().split())
def is_onjun(n):
    if not i%2:
        return False
    elif not i%5:
        return False
    elif not i%3 and i%9:
        return False
    return True
cnt =0
for i in range(a,b+1):
    if is_onjun(i):
        cnt +=1
print (cnt)