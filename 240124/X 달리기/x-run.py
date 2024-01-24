x = int(input())
cnt =0
time =0
speed =1
a=1
flag = False
while (1):
    time +=1
    cnt += speed
    if cnt  >= x//2 and not flag:
        a =-1
        flag = True
    if speed ==1 and flag:
        a =0
    speed +=a
    
    if cnt >= x:
        break
print(time)