arr=[list(map(int,input().split())) for _ in range(19)]

dxs = [0,1,1,1]
dys = [1,0,1,-1]
def in_range(x,y):
    return 0<x<19 and 0<y<19

def is_answer():
    for i in range(19):
        for j in range(19):
            if arr[i][j] !=0:
                for dx,dy in zip(dxs,dys):
                    x,y = i,j
                    cnt=1
                    while (1):
                        nx = x+dx
                        ny = y+dy
                        if not in_range(nx,ny):
                            break
                        if arr[nx][ny] != arr[x][y]:
                            break
                        cnt +=1
                        x = nx
                        y = ny
                    if cnt ==5:
                        print(arr[i][j])
                        print(i+2*dx+1,j+2*dy+1)
                        return
    print(0)
    return
is_answer()