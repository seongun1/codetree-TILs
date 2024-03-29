n = 0
sum_n = 0
tmp1 = int(input())
cnt =0
tmp = list(map(int,input().split()))
for t in tmp:
    if (n >200):
        break
    n += t
    cnt +=1
print(n)
print(f'{n/cnt}')