n,t = map(int,input().split())

up_arr = list(map(int,input().split()))
mid_arr = list(map(int,input().split()))
down_arr = list(map(int,input().split()))

down_arr.reverse()

for _ in range(t):

    up_temp = up_arr[-1]
    mid_temp = mid_arr[-1]
    down_temp = down_arr[0]
    #print("up_temp : {}, under_temp : {}".format(up_temp, under_temp))

    for i in range(n-1,0,-1):
        up_arr[i] = up_arr[i-1]
        mid_arr[i] = mid_arr[i-1]

    for i in range(n-1):
        down_arr[i] = down_arr[i+1]

    up_arr[0] = down_temp
    mid_arr[0] = up_temp
    down_arr[-1] = mid_temp

down_arr.reverse()

print(*up_arr)
print(*mid_arr)
print(*down_arr)