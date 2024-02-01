n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n
max_cnt =0
for i in range(n-2):
    for j in range(n-2):
        cnt =0
        flag = True
        for k in range(3):
            for p in range(3):
                if in_range(i+k,j+p) and arr[i+k][j+p] == 1:
                    cnt +=1
                if not in_range(i+k,j+p):
                    flag = False
                    break
            if not flag:
                break
        max_cnt = max(cnt,max_cnt)
print(max_cnt)