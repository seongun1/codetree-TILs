n=int(input())
a1,b1,c1 = map(int,input().split())
a2,b2,c2 = map(int,input().split())
cnt =0
a=[]
b=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if (abs(i-a1)<=2 or abs(i-a1)>=n-2) and (abs(j-b1)<=2 or abs(j-b1)>=n-2) and (abs(k-c1) <=2 or abs(k-c1) >= n-2):
                cnt +=1
            elif (abs(i-a2)<=2 or abs(i-a2)>=n-2) and (abs(j-b2)<=2 or abs(j-b2)>=n-2) and (abs(k-c2) <=2 or abs(k-c2) >= n-2):
                cnt +=1
print(cnt)