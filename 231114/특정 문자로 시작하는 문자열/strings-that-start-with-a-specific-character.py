n=int(input())
arr=[input() for _ in range(4)]
tmp= input()
tmp_len =0
cnt=0
for a in arr:
    if a[0] == tmp:
        cnt +=1
        tmp_len += len(a)
if cnt !=0:
    print(f"{cnt} {(tmp_len / cnt):.2f}")
else:
    print(0,0.00)