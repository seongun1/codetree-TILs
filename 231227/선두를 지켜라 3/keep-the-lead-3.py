n,m = map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(m):
    b.append(list(map(int,input().split())))
tmp=1000000 #총 걸린 시간

arr_a= [0 for i in range(tmp+1)]
arr_b= [0 for i in range(tmp+1)]
time_a =1
for i in range(len(a)):
    v,t = map(int,a[i])
    for i in range(time_a,time_a+t):
        arr_a[i] = arr_a[i-1] +v
    time_a += t
time_b = 1
for i in range(len(b)):
    v,t = map(int,b[i])
    for i in range(time_b,time_b+t):
        arr_b[i] = arr_b[i-1] +v
    time_b += t

cnt =0

arr=[-1 for i in range(tmp+1)]
for i in range(1,tmp+1):
    if arr_a[i] > arr_b[i]:
        arr[i] = 1
    elif arr_a[i] < arr_b[i]:
        arr[i] = 2
    else:
        arr[i] = 0
for i in range(2,tmp+1):
    if arr[i-1] != arr[i]:
        cnt +=1
print(cnt)