a,b,c=map(int,input().split())
tmp =a*b*c
def mul_val(a):
    if a<10:
        return a
    return mul_val(a//10) + a%10
print(mul_val(tmp))