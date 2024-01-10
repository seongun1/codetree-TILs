x,y = map(int,input().split())

cnt =0
for i in range(x,y+1):
    i = str(i)
    tmp=[]
    for j in i:
        tmp.append(int(j))

    dict_arr ={}
    for t in tmp:
        if t in dict_arr:
            dict_arr[t] +=1
        else:
            dict_arr[t] =1
    arr =list(dict_arr.values())
    arr.sort()
    if len(arr) == 2 and (arr[1] == len(tmp) -1 and arr[0] == 1):
        cnt +=1    
    
print(cnt)