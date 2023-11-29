class person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

arr=[]
for i in range(5):
    n,h,w = input().split()
    h = int(h)
    w=float(w)
    arr.append(person(n,h,w))

arr.sort(key=lambda x: x.name)
print('name')

for a in arr:
    print(f"{a.name} {a.height} {a.weight:.1f}")

print()
arr.sort(key = lambda x : (-x.height))
print('height')

for a in arr:
    print(f"{a.name} {a.height} {a.weight:.1f}")