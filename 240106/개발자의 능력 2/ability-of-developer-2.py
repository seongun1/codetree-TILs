import sys
arr= list(map(int,input().split()))
num1,num2,num3 = 0,0,0
min_ans = sys.maxsize
for i in range(6):
    for j in range(i+1,6):
        num1 = arr[i]+arr[j]
        for k in range(6):
            for p in range(k+1,6):
                if i==k or i==p or j==k or j==p:
                    continue
                num2 =arr[k] + arr[p]
                num3 = sum(arr) - num1 - num2
                tmp=[]
                tmp.append(num1)
                tmp.append(num2)
                tmp.append(num3)
                tmp.sort()
                ans = tmp[2] - tmp[0]
                min_ans = min(ans,min_ans)
print(min_ans)