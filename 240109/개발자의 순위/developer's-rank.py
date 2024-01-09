k,n = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(k)]
cnt =0
for j in range(n):
    for k in range(j+1,n):
        a = arr[0][j]
        b = arr[0][k]
        flag = True
        s1,s2 = 0,0
        for p in range(1,len(arr)):
            for s in range(n):
                if a == arr[p][s]:
                    s1 =s
                if b == arr[p][s]:
                    s2 = s
            if s1 > s2:
                flag = False
                break
        if flag:
            cnt +=1
print(cnt)