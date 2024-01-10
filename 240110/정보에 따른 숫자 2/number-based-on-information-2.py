t,a,b =map(int,input().split())
#d1이 d2보다 같거나 작은 경우 x= k는 특별한 위치
s=[0] * (1001)
n=[0] * (1001)
for _ in range(t):
    char , idx = input().split()
    idx = int(idx)
    if char =='S':
        s[idx] = 1
    elif char == 'N':
        n[idx] = 1
cnt =0
for i in range(a,b+1):
    d1,d2 = 1000,1000
    for p in range(len(s)):
        if s[p] == 1 and d1 > abs(i - p):
            d1 =abs(i-p)
    for k in range(len(n)):
        if n[k] ==1 and d2 > abs(i - k):
            d2 = abs(i-k)
    if d1 <= d2:
        cnt +=1
print(cnt)