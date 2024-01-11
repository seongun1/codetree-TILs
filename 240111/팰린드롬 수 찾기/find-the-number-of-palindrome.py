x,y = map(int,input().split())
cnt =0

def is_pelindrom(tmp):
    for i in range(len(tmp)//2):
        if tmp[i] != tmp[len(tmp)-1-i]:
            return False
    return True
for i in range(x,y+1):
    tmp= list(map(int,str(i)))
    if is_pelindrom(tmp):
        cnt +=1
print(cnt)