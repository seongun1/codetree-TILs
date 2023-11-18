a,b=map(int,input().split())
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if not n%i:
            return False
    return True
ans =0
for i in range(a,b+1):
    if is_prime(i):
        ans +=i
print(ans)