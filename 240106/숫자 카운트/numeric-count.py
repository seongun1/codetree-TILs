n=int(input())
arr=[]
for _ in range(n):
    n,a,b = map(int,input().split())
    n=list(map(int,str(n)))
    arr.append([n[0],n[1],n[2],a,b])


cnt=0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or j==k or k ==i:
                continue
            flag =True
            for a in arr:
                cnt1=0
                cnt2=0
                candidate =[i,j,k]
                for x in range(3):
                    for y in range(3):
                        if a[x] == candidate[y]:
                            if x==y: #스트라이크
                                cnt1 +=1
                            elif x!=y: #볼
                                cnt2 +=1
                if cnt1 != a[3] or cnt2 !=a[4]:
                    flag =False
            if flag:
                cnt +=1
print(cnt)