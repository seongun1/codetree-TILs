import sys
m1,d1,m2,d2 = map(int,input().split())
a= input()
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cnt_date(m1,d1,m2,d2):
    t1,t2 = 0,0
    for i in range(1,m1):
        t1 += num_of_days[i]
    t1 += d1
    for i in range(1,m2):
        t2 += num_of_days[i]
    t2 += d2
    return t2 - t1 
    
arr=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
total_days = cnt_date(m1,d1,m2,d2) - arr.index(a)
count =0
if total_days >= 0:
    count +=1
else:
    print(count)
    exit(0)
count += total_days //7
print(count)