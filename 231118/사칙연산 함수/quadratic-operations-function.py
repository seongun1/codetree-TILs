a,o,c=input().split()
a,c = int(a),int(c)
def add(a,b):
    return a+b
def mod (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return int(a,b)

if o =='+':
    print(f"{a} + {c} = {add(a,c)}")
elif o =='-':
    print(f"{a} - {c} = {mod(a,c)}")
elif o == '*':
    print(f"{a} * {c} = {mul(a,c)}")
elif o == '/':
    print(f"{a} / {c} = {div(a,c)}")
else:
    print('False')