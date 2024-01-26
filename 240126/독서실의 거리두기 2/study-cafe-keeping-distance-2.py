n=int(input())
arr= str(input())
arr = list(arr)
import sys
def cnt_min_dist(n):
    min_dist = sys.maxsize
    for i in range(n):
        if arr[i] =='1':
            dist=sys.maxsize
            for j in range(i+1,n):
                if arr[j] =='1':
                    dist = j-i
                    break
            min_dist = min(dist,min_dist)
    return min_dist

dist =0
index_i,index_j = 0,0
flag = False
for i in range(n):
    if arr[i] == '1':
        for j in range(i+1,n):
            if arr[j] =='1':
                if j-i > dist:
                    dist = j-i
                    index_i,index_j = i,j
                break
            if j == n-1:
                if (j-i) * 2> dist:
                    dist = j-i
                    index_i,index_j = i,j
                    flag =True
                break
if not flag:
    arr[(index_i + index_j) //2] ='1'
else:
    arr[n-1] ='1'

print(cnt_min_dist(n))