n=int(input())
class student:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng

arr=[]
for _ in range(4):
    n,k,e,m = input().split()
    k,e,m = int(k),int(e),int(m)
    arr.append(student(n,k,e,m))

arr.sort(key =lambda x : (-x.kor,-x.eng,-x.math))
for a in arr:
    print(a.name,a.kor,a.eng,a.math)