import sys
arr=list(map(int,input().split()))
num1,num2,num3=0,0,0
ans =0
min_ans = sys.maxsize
a= arr[0]
flag = True
for i in range(len(arr)):
    if a != arr[i]:
        flag = False
        break
if flag:
    print(-1)
    sys.exit()


for i in range(5):
    for j in range(i+1,5):
        num1 = arr[i] + arr[j]
        for k in range(5):
            for p in range(k+1,5):
                if i==k or i==p or j==k or j==p:
                    continue
                num2 = arr[k] + arr[p]
                num3 = sum(arr) - num1 - num2
                if num1 == num2 or num2 ==num3 or num1 == num3:
                    continue
                tmp=[]
                tmp.append(num1)
                tmp.append(num2)
                tmp.append(num3)
                tmp.sort()
                ans = tmp[2] - tmp[0]
                min_ans =min(ans,min_ans)
            
print(min_ans)