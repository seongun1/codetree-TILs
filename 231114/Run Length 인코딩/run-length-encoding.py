arr =list(input())
index =0
cnt =1
tmp=''
while (index != len(arr)-1):
    cnt =0
    for j in range(index,len(arr)):
        if arr[index] == arr[j]:
            cnt +=1
        else:
            break
    tmp += arr[index]+str(cnt)
    index =j
    if index == len(arr)-1 and arr[index] != arr[index-1]:
        tmp += arr[index] + '1'
if (len(arr) ==1):
    tmp += arr[index]+'1'
print(len(tmp))
print(tmp)