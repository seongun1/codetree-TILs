a,b= map(int,input().split())
def mul(a,b):
    x = max(a,b)
    y = min(a,b)
    return (x+25 , y*2)
if a>b:
    a,b = mul(a,b)
else:
    b,a =mul(a,b)
print(a,b)