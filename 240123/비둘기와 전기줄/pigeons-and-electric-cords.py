n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
tmp = [2] * 101
cnt =0
for a1,b1 in arr:
    if tmp[a1] != b1 and tmp[a1] != 2:
        cnt +=1
    tmp[a1] = b1
print(cnt)