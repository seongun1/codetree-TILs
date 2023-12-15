n,m = map(int,input().split())
a=[0] * 1000000
b=[0] * 1000000
time =1
for _ in range(n):
    v,t = map(int,input().split())
    for i in range(time,time+t):
        a[i] = a[i-1] + v
    time +=t
time=1

for _ in range(m):
    v,t = map(int,input().split())
    for i in range(time,time+t):
        b[i] = b[i-1] + v
    time +=t
cnt =0
for i in range(1,time):
    if a[i-1] >= b[i-1] and a[i] < b[i]:
        cnt +=1
    elif a[i-1] <= b[i-1] and a[i] > b[i]:
        cnt +=1
cnt -=1
print(cnt if cnt >0 else 0)