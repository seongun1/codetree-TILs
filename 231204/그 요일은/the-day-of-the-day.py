m1,d1,m2,d2 = map(int,input().split())
a= input()
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cnt_date(m1,d1,m2,d2):
    t1,t2 = 0,0
    for i in range(1,m1):
        t1 += num_of_days[m1]
    t1 += d1
    for i in range(1,m2):
        t2 += num_of_days[m2]
    t2 += d2
    return t2 - t1
arr=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day = arr.index(a)

day_left = cnt_date(m1,d1,m2,d2)-day
print(day,day_left)

if day_left>=0:
    count = 1
else:
    count =0

count += day_left //7
print(count)