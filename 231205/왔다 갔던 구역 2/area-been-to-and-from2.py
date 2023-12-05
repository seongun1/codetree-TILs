n= int(input())
pin =1000
arr=[0 for _ in range(2001)]
for _ in range(n):
    move,order = input().split()
    move = int(move)
    if order =='L':
        for i in range(pin-1,pin-move-1,-1):
            arr[i] +=1
        pin -= move
    elif order =='R':
        for k in range(pin,pin+move):
            arr[k] +=1
        pin += move
        
cnt =0
for a in arr:
    if a>1:
        cnt +=1
print(cnt)