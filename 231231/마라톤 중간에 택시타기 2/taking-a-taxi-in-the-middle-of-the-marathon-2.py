import sys
n=int(input())
def cal_distance (x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

a=[list(map(int,input().split())) for _ in range(n)]
min_dis = sys.maxsize
cnt =1
while (cnt <len(a)-1):
    distance =0
    previous =0
    for i in range(1,len(a)):
        if i == cnt:
            continue
        distance += cal_distance(a[previous][0],a[previous][1],a[i][0],a[i][1])
        previous =i
    min_dis = min(min_dis,distance)
    cnt +=1
print(min_dis)