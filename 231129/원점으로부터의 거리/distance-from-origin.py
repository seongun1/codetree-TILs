import math
n=int(input())

class dis:
    def __init__(self,x,y,seq):
        self.x = x
        self.y =y
        self.seq = seq
arr=[]
for i in range(1,n+1):
    x,y = map(int,input().split())
    arr.append(dis(x,y,i))

arr.sort(key = lambda k : (math.sqrt(pow(k.x,2) + pow(k.y,2)),k.seq))

for a in arr:
    print(a.seq)