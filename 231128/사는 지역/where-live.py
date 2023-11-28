class home:
    def __init__(self,name,adress,location):
        self.name = name
        self.adress = adress
        self.location = location

n=int(input())
tmp =[]
for i in range(n):
    h,a,l = input().split()
    tmp.append(home(h,a,l))

max_val = 0
for i in range(n):
    if tmp[max_val].name < tmp[i].name:
        max_val = i
print(f"name {tmp[max_val].name}")
print(f"addr {tmp[max_val].adress}")
print(f"city {tmp[max_val].location}")