x,y = map(int,input().split())
arr =[list(input().split()) for _ in range(x)]
nx,ny = 0,0
cnt =0
for i in range(1,x):
    for j in range(1,y):
        for k in range(i+1,x-1):
            for l in range(j+1,y-1):
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[x-1][y-1]:
                    cnt +=1
print(cnt)