n=int(input())
class student:
    def __init__(self,height,weight,num):
        self.height = height
        self.weight = weight
        self.num = num
arr=[]
for i in range(1,n+1):
    h,w = map(int,input().split())
    arr.append(student(h,w,i))

arr.sort(key = lambda x : (-x.height,-x.weight,x.num))

for a in arr:
    print(a.height,a.weight,a.num)