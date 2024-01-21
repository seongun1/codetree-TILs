a,b = map(int,input().split())
ans =0
cnt =0
for i in range(a,b+1):
    if not i%5:
        ans += i 
        cnt +=1
    if not i%7:
        ans +=i
        cnt +=1
    if not i%35:
        ans -= i
        cnt -=1
print (f"{ans} {(ans / cnt):.1f}")