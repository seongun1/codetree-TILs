a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
def is_bubun(a,b,an,bn):
    flag = False
    for i in range(an-bn+1):
        if a[i] == b[0]:
            flag =True
            for j in range(bn):
                if a[i+j] != b[j]:
                    flag =False
                    break
            return True
    return False


if is_bubun(arr,brr,a,b):
    print('Yes')
else:
    print('No')