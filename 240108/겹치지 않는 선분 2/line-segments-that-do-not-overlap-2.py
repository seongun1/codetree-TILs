n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
cnt = [True] * (n)

for i in range(n):
    for j in range(n):
        x1,x2 = arr[i]
        x3,x4 = arr[j]
        if i==j:
            continue
        
        if (x1 < x2 and x3 < x4) : #기울기 +,+
            if x3 < x1 < x2 < x4 or x1<x3 <x4 <x2:
                cnt[i] = False
                cnt[j] = False
        elif (x1 > x2 and x3 >x4): #기울기 -,-
            if x4 < x2 <= x3 <x1 or x2 < x4 <= x1 <x3:
                cnt[i] =False
                cnt[j] =False
        elif(x1 < x2 and x3 > x4): #기울기 +,-
            if x1 < x3 and x4 < x2:
                cnt[i] = False
                cnt[j] = False  
        elif (x2 < x1 and x3 < x4): #기울기 -,+
            if x1 > x3 and x2 <x4 :
                cnt[i] =False
                cnt[j] =False

ans=0
for i in range(len(cnt)):
    if cnt[i] == True:
        print(i)
        ans +=1
print(ans)