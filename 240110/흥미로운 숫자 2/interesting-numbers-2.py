x,y = map(int,input().split())

cnt =0
for i in range(x,y+1):
    i = str(i)
    tmp=[]
    for j in i:
        tmp.append(int(j))
    tmp = set(tmp)
    

print(cnt)