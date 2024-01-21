arr = [int(input()) for _ in range(10)]

ans=0
cnt=0
for a in arr:
    if 0<=a<=200:
        ans +=a
        cnt +=1
    
print(f"{ans} {ans/cnt:.1f}")