a,b= map(int,input().split())
def is_prime(n):
    for i in range(2,n):
        if not n%i:
            return False
    return True
def is_even(n):
    n=str(n)
    tmp =0
    for i in n:
        tmp += int(i)
    if tmp%2:
        return False
    else:
        return True
cnt =0
for i in range(a,b+1):
    if is_even(i) and is_prime(i):
        cnt +=1
print(cnt)