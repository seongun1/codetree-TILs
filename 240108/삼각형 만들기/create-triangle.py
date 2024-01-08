n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
max_area =0
for i in range(n):
    for j in range(i+1,n):
        tmp=[]
        for k in range(j+1,n):
            tmp.append(arr[i])
            tmp.append(arr[j])
            tmp.append(arr[k])
            if tmp[0][1] != tmp[1][1] and tmp[0][1] != tmp[2][1] and tmp[1][1] != tmp[2][1] :
                tmp=[]
                continue
            if tmp[0][0] != tmp[1][0] and tmp[0][0] != tmp[2][0] and tmp[1][0] != tmp[2][0]:
                tmp=[]
                continue
            area = abs((tmp[0][1]*tmp[1][1] + tmp[1][0]*tmp[2][1] + tmp[2][0]*tmp[0][1]) - (tmp[1][0]*tmp[0][1] + tmp[2][0]*tmp[1][1] + tmp[0][0]*tmp[2][1]))
            max_area  = max(max_area,area)
            tmp=[]
print(max_area)