n = int(input())
arr= str(input())
arr= list(arr)
max_dist=0
index_i ,index_j = 0,0
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

for i in range(n):
    if arr[i] == '1':
        dist =0
        for j in range(i+1,n):
            if arr[j] =='1':
                dist = j-i
                break
        max_dist = max(dist,max_dist)
        if max_dist == dist:
            index_i ,index_j = i,j

arr[(index_i + index_j) //2] ='1'
print(cnt_min_dist(n))