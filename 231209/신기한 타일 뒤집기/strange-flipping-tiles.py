n=int(input())
arr= [0 for i in range(200000)]
MAX = 100000
point =MAX

for _ in range(n):
    x,dis = input().split()
    x = int(x)
    if dis == 'L':
        for i in range(point,point-x,-1):
            arr[i] = 1 #white
        point =point-x+1
    elif dis == 'R':
        for i in range(point,point+x):
            arr[i] = 2 #black
        point =point + x-1
           
white,black =0,0
for a in arr:
    if a == 1:
        white +=1
    elif a == 2:
        black +=1
print (white,black)