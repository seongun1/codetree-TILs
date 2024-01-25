n=int(input())
arr= [list(map(int,input().split())) for _ in range(n)]

win =0

def win_cnt(a,b):
    global win
    if a==1 and b ==3:
        win +=1
    if a==2 and b ==1:
        win +=1
    if a==3 and b ==2:
        win +=1
    return win


def turn_val():
    for i in range(len(arr)):
        arr[i][0],arr[i][1] = (arr[i][0] %3) +1 , (arr[i][1] %3) +1

def change_val():
    for i in range(len(arr)):
        arr[i][0],arr[i][1] = arr[i][1],arr[i][0]
max_cnt =0
for _ in range(3):
    cnt =0
    for a,b in arr:
        cnt = win_cnt(a,b)
    turn_val()
    max_cnt = max(cnt,max_cnt)
    win =0
turn_val()
change_val()
for _ in range(3):
    cnt =0
    for a,b in arr:
        cnt = win_cnt(a,b)
    turn_val()
    max_cnt = max(cnt,max_cnt)
    win =0

print(max_cnt)