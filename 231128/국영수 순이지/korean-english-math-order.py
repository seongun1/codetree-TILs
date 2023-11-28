n=int(input())
class student:
    def __init__(self,name,kor,math,eng):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng

arr=[]
for _ in range(4):
    n,k,m,e = input().split()
    k,m,e = int(k),int(m),int(e)
    arr.append(student(n,k,m,e))

arr.sort(key =lambda x : (-x.kor,-x.math,-x.eng))
for a in arr:
    print(a.name,a.kor,a.math,a.eng)