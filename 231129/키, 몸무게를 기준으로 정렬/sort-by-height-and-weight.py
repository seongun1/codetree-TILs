n=int(input())

class person:
    def __init__(self,name,height,weight):
        self.name = name 
        self.height = height
        self.weight = weight
arr=[]
for _ in range(n):
    n,h,w = input().split()
    arr.append(person(n,int(h),int(w)))

arr.sort(key = lambda x : (x.height,-x.weight))
for a in arr:
    print (a.name,a.height,a.weight)