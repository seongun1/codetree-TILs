n=int(input())
arr=[]
block =0
for _ in range(n):
    arr.append(int(input()))
target = sum(arr) // n
tmp = []
for a in arr:
    tmp.append(a - target)
cnt =0
for t in tmp:
    if t>=0:
        cnt +=t
print(cnt)