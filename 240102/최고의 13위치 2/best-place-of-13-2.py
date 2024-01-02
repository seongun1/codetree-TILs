n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visit =[[False] * n for _ in range(n)]
max_coin =0
coin =0
visit_x,visit_y = 0,0
for i in range(n):
    for j in range(n-2):
        coin = arr[i][j] + arr[i][j+1]+arr[i][j+2]
        max_coin = max(coin,max_coin)
        if coin == max_coin:
            #기존의 visit 은 False
            visit[visit_x][visit_y],visit[visit_x][visit_y+1],visit[visit_x][visit_y+2] =  False,False,False
            #새로운 곳을 True 처리
            visit_x = i
            visit_y = j
            visit[visit_x][visit_y],visit[visit_x][visit_y+1],visit[visit_x][visit_y+2] =  True,True,True
        coin =0

max_coin2= 0
for i in range(n):
    coin=0
    for j in range(n-2):
        if not visit[i][j] and not visit[i][j+1] and not visit[i][j+2]:
            coin = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            max_coin2 =max(coin,max_coin2)
            coin=0
print(max_coin+max_coin2)