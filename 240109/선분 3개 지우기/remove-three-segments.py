n = int(input())
arr = [0] * (101)

def check(arr):
    for a in arr:
        if a>=2:
            return False
    return True

line = [list(map(int,input().split())) for _ in range(n)]
cnt =0
for i in range(n):
    for j in range(i+1,n):
        for k in range (j+1,n):
            flag = True
            for paint in range(n):
                if paint == i or paint == j or paint == k:
                    continue
                a,b = line[paint]
                for s in range(a,b+1):
                    arr[s] +=1
            if check(arr):
                cnt +=1
            arr = [0] * (101)
            
print(cnt)