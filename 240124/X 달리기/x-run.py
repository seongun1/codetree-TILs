x = int(input())

speed =1
dist =0
time =0
while (dist < x):
    dist += speed
    if (x - dist) >= (speed+1) * (speed +2) /2:
        speed +=1
    elif (x - dist)  >= (speed) * (speed+1) /2:
        speed = speed
    elif x - dist >= (speed) * (speed -1) /2:
        speed -=1
    if speed <=1:
        speed =1
    time +=1
print(time)