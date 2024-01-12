n=int(input())

points = [list(map(int,input().split())) for _ in range(n)]
arr= [0]*5
max_point =101
for x_line in range(2,101,2): #y축에 평행한 직선
    for y_line in range(2,101,2): #x축에 평행한 직선
        for x,y in points:
            if x < x_line and y<y_line:
                arr[1] +=1
            elif x>x_line and y<y_line:
                arr[2] +=1
            elif x < x_line and y>y_line:
                arr[3] +=1
            elif x > x_line and y>y_line:
                arr[4] +=1
        max_point = min(max_point,max(arr))
        arr = [0] *5

print(max_point)