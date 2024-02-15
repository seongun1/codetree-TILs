n,t = map(int,input().split())

up_arr = list(map(int,input().split()))
under_arr = list(map(int,input().split()))

under_arr.reverse()

for _ in range(t):

    up_temp = up_arr[-1]
    under_temp = under_arr[0]
    #print("up_temp : {}, under_temp : {}".format(up_temp, under_temp))

    for i in range(n-1,0,-1):
        up_arr[i] = up_arr[i-1]

    for i in range(n-1):
        under_arr[i] = under_arr[i+1]

    up_arr[0] = under_temp
    under_arr[-1] = up_temp

    #print("up_arr : {}, under_arr : {}".format(up_arr, under_arr))

under_arr.reverse()
print(*up_arr)
print(*under_arr)