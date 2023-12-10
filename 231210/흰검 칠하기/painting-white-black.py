n=int(input())
MAX = 100000
point =MAX
arr = [0 for _ in range(2*MAX +1)]
arr_grey = [0 for _ in range(2*MAX +1)]
for _ in range(n):
    x,dire = input().split()
    x = int(x)
    if dire == 'L':
        for i in range(point,point-x,-1):
            arr[i] =1
            arr_grey[i] +=1
        point = point - x +1
    elif dire =='R':
        for i in range(point,point+x):
            arr[i] =2
            arr_grey[i] += 2
        point = point +x -1
white,black,grey = 0,0,0
for i in range(len(arr)):
    if arr_grey[i] >= 6:
        grey +=1
        arr[i] = 0
    if arr[i] ==1:
        white +=1
    elif arr[i] ==2:
        black +=1
print(white,black,grey)