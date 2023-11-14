arr =input()
tmp =''
i=0
while (i != len(arr)-1):
    cnt=1
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            cnt +=1
        else:
            break
    tmp += arr[i] + str(cnt)
    i=j 
print(len(tmp),tmp,sep="\n")