arr=[input() for i in range(10)]
tmp = input()
cnt =0
for a in arr:
    if a[-1] ==tmp:
        print(a)
        cnt +=1
if cnt ==0:
    print('None')