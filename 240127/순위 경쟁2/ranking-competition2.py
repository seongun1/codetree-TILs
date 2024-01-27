n=int(input())
arr = [list(input().split()) for _ in range(n)]

sum_a , sum_b = 0,0
tmp =[]
tmp.append('AB')

for c,s in arr:
    if c =='A':
        sum_a += int(s)
    elif c == 'B':
        sum_b += int(s)
    if sum_a > sum_b:
        tmp.append('A')
    elif sum_a < sum_b:
        tmp.append('B')
    elif sum_a == sum_b:
        tmp.append('AB')
cnt =0

for i in range(n):
    if tmp[i] !=tmp[i+1]:
        cnt +=1
print(cnt)