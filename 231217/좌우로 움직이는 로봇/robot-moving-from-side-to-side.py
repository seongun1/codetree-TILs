n,m = map(int,input().split())
point =1000000

a=[point] * point
b=[point] * point
time_a =1
for _ in range(n):
    t,d = input().split()
    t= int(t)
    if d =='L':
        for i in range(time_a,t+time_a):
            a[i] = a[i-1] -1
        time_a += t
    elif d =='R':
        for i in range(time_a,t+time_a):
            a[i] = a[i-1] + 1
        time_a +=t


time_b =1
for _ in range(m):
    t,d = input().split()
    t = int(t)
    if d=='L':
        for i in range(time_b,t+time_b):
            b[i] = b[i-1] -1
        time_b +=t
    elif d == 'R':
        for i in range(time_b,t+time_b):
            b[i] = b[i-1] + 1
        time_b +=t


if time_a>time_b:
    for i in range(time_b,time_a):
        b[i] = b[i-1]
elif time_a<time_b:
    for i in range(time_a,time_b):
        a[i] =a[i-1]

def print_arr(a,length):
    for i in range(length):
        print(a[i],end=' ')
    print()
cnt =0

for i in range(1,max(time_a,time_b)):
    if a[i-1] != b[i-1] and a[i] == b[i]:
        cnt +=1
print(cnt)