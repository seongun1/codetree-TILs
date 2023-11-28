n=int(input())
class weather:
    def __init__(self,date,day,whea):
        self.date = date
        self.day = day
        self.whea = whea
arr=[]
for _ in range(n):
    x,y,z = input().split()
    arr.append(weather(x,y,z))

rain=[]
for a in arr:
    if a.whea =="Rain":
        rain.append(a)
min_val = 0
for i in range(1,len(rain)):
    if rain[min_val].date > rain[i].date:
        min_val = i
print(rain[min_val].date , rain[min_val].day,rain[min_val].whea)