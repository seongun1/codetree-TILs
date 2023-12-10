n=int(input())
MAX = 100000
point =MAX
arr = [0 for _ in range(2*MAX +1)]
arr_white =[0 for _ in range(2*MAX +1)]
arr_black = [0 for _ in range(2*MAX +1)]
grey = 0
for _ in range(n):
    x,dire = input().split()
    x = int(x)
    if dire == 'L':
        for i in range(point,point-x,-1):
            arr[i] = 1
            arr_white[i] +=1
        point = point - x +1
    elif dire =='R':
        for i in range(point,point+x):
            arr[i] = 2
            arr_black[i] +=1
        point = point +x -1

black,white = 0,0
for i in range(len(arr_black)):
    if arr_white[i] >= 2 and arr_black[i] >= 2:
        grey +=1
        arr_black[i] =0
        arr_white[i] =0
    elif arr[i] == 2:
        black +=1
    elif arr[i] ==1:
        white +=1
print(white,black,grey)