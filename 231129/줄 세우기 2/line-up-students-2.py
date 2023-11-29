class studert:
    def __init__(self,seq,h,w):
        self.seq = seq
        self.h = h
        self.w = w
arr=[]
n=int(input())
for i in range(n):
    h,w =map(int,input().split())
    arr.append(studert(i+1,h,w))

arr.sort(key = lambda x : (x.h,-x.w))
for a in arr:
    print (a.h,a.w,a.seq)