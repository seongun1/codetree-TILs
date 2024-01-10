n,c,g,h = map(int,input().split()) #장비의 갯수 N  온도에 따른 장비들의 작업량 c/g/h

arr=[list(map(int,input().split())) for _ in range(n)]

def cnt_work(i,a,b):
    if i<a:
        return c
    elif a<= i <=b:
        return g
    elif i>b:
        return h
max_work=0
for temp in range(1001):
    work =0
    for i in range(n):
        work += cnt_work(temp,arr[i][0],arr[i][1])
    max_work =max(work,max_work)
print(max_work)