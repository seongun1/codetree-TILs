n=int(input())
cnt =0
a,b,c = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if abs(i-a) >2 and abs(j-b) >2 and abs(k-c)>2:
                cnt +=1
print(n**3 - cnt)