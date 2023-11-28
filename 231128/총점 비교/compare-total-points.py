n=int(input())
class student:
    def __init__(self,name,b1,b2,b3):
        self.name = name
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
arr=[]
for i in range(n):
    n,a,b,c = input().split()
    a,b,c = int(a),int(b),int(c)
    arr.append(student(n,a,b,c,))
arr.sort(key=lambda x : x.b1+x.b2+x.b3)
for a in arr:
    print(a.name,a.b1,a.b2,a.b3)