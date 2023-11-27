class agent:
    def __init__(self,name,score):
        self.name= name
        self.score = score

tmp=[]
for i in range(5):
    name,score = input().split()
    score= int(score)
    tmp.append(agent(name,score))

tmp = sorted(tmp,key = lambda x : x.score)
print (tmp[0].name , tmp[0].score)