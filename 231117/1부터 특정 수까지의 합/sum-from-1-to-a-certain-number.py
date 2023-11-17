n=int(input())
def ans(a):
    tmp =0
    for i in range(a+1):
        tmp += i
    return (tmp // 10)
print(ans(n))