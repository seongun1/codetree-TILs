n,m = map(int,input().split())
arr= list(map(int,input().split()))

cnt =0
point =0
visited=[False] * n
while(1):
    if arr[point] == 1:
        #print(cnt)
        cnt +=1
        visited[point] = True
        for i in range(point+1,n):
            if i-point <=2*m:
                visited[i] = True
                continue
            elif i-point>2*m:
                point = i
                break
    else:
        point +=1
    #print(visited,point)
    if visited[-1]:
        break
print(cnt)