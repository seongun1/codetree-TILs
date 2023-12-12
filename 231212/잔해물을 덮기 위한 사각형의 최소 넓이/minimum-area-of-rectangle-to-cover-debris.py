x1,y1,x2,y2 = map(int,input().split())
z1,w1,z2,w2 = map(int,input().split())
arr = [[0] * 2000 for _ in range(2000)]
x1,y1,x2,y2 = 1000+x1,1000+y1,1000+x2,1000+y2
z1,w1,z2,w2 = 1000+z1,1000+w1,1000+z2,1000+w2

def print_arr():
    for i in range(x1,x2):
        for j in range(y1,y2):
            print(arr[i][j],end=' ')
        print()

for i in range(x1,x2):
    for j in range(y1,y2):
        arr[i][j] =+1

for i in range(z1,z2):
    for j in range(w1,w2):
        arr[i][j] = 0
cnt_h =[]
tmp =0
for i in range(x1,x2):
    if arr[i][y1] ==1:
        tmp +=1
cnt_h.append(tmp)
tmp =0
for i in range(x1,x2):
    if arr[i][y2-1] ==1:
        tmp +=1
cnt_h.append(tmp)
tmp =0
cnt_w=[]
for i in range(x1,x2):
    for j in range(y1,y2):
        if arr[i][j] == 1:
            tmp +=1
    cnt_w.append(tmp)
    tmp=0

print(max(cnt_h) * max(cnt_w))