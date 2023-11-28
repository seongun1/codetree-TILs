a = input().split()

class product:
    def __init__(self,name,code):
        self.name = name
        self.code = code
p1 = product("codetree",50);
p2 = product(a[0],a[1])
print(f"product {p1.code} is {p1.name}")
print(f"product {p2.code} is {p2.name}")