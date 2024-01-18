n=int(input())
arr=str(input())
arr=list(arr)
import sys
ans =0
for i in range(n):
    for j in range(n):
        if arr[i] =='1' or arr[j] == '1' or i==j:
            continue
        arr[i] = '1'
        arr[j] = '1'
        #거리계산
        dis = sys.maxsize
        for k in range(n):
            for p in range(n):
                if arr[p] =='0' or p ==k or arr[k] == '0':
                    continue
                if abs(k-p) < dis:
                    dis = abs(k-p)
        ans = max(dis,ans)
        arr[i] ='0'
        arr[j] ='0'
print(ans)