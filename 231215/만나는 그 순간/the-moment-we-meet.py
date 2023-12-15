n,m = map(int,input().split())
a= [0 for _ in range(1000000)]
b=[0 for _ in range(1000000)]

def cal_range(n,a):
    start =0 #시작점
    global second
    second =1
    for _ in range(n):
        d,t =input().split()
        t=int(t)
        if d =='R':
            for i in range(second,t+second):
                start +=1
                a[i] = start
            second +=t
        elif d =='L':
            for i in range(second,t+second):
                start -=1
                a[i] = start
            second +=t
    return a
a= cal_range(n,a)
b = cal_range(m,b)

def cal_second():
    for i in range(1,second):
        if a[i] == b[i]:
            return i
    return -1
print(cal_second())