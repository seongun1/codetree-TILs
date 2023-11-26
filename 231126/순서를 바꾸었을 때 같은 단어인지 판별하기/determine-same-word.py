a= input()
a=list(a)
b= input()
b=list(b)
a.sort()
b.sort()

def if_same():
    for u,i in zip(a,b):
        if u != i:
            return "No"
    return "Yes"
print(if_same())