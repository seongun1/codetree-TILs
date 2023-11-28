n=int(input())
class person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
arr=[]
for _ in range(n):
    name,height,weight =input().split()
    arr.append(person(name,height,weight))

arr.sort(lambda x: x.height)
for a in arr:
    print(a.name,a.height,a.weight)