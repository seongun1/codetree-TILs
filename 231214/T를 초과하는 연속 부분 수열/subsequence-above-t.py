n,t=map(int,input().split())
arr=list(map(int,input().split()))
tmp=[]
def answer(n,t):
    cnt =1
    if n==1:
        if arr[i] <= t:
            return 0
        else:
            return 1
    else:
        if max(arr) <= t:
            return 0
        else:
            for i in range(n):
                if arr[i] > t and arr[i-1] >t:
                    cnt +=1
                    tmp.append(cnt)
                else:
                    cnt =1
                    tmp.append(cnt)
            return max(tmp)
print(answer(n,t))