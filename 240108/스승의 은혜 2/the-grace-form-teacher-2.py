n,b = map(int,input().split())

arr=[int(input()) for _ in range(n)]

max_cnt =0
money =b
for i in range(n):
    arr[i] /=2
    money =b
    cnt=0
    
    for j in range(n):
        if i==j:
            continue
        if money>=arr[j]:
            cnt +=1
            money -=arr[j]
        else:
            continue
    max_cnt = max(cnt,max_cnt)
print(max_cnt)