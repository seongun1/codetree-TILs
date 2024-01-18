n= int(input())
arr=list(map(int,input().split()))

for i in range(n):
    tmp =[0 for _ in range(n)]
    tmp[0] = i+1
    exist = [False for _ in range(n+1)]
    flag =True
    for j in range(n-1):
        a = arr[j] - tmp[j]
        if a <=0 or a>n:
            flag = False
            break
        if exist[a]:
            flag = False
            break
        tmp[j+1] = a
        exist[a] = True
    if flag:
        print(*tmp)
        break