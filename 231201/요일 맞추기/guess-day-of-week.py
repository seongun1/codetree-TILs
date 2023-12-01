num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cnt_day(m1,d1,m2,d2):
    tmp1,tmp2 =0,0
    for i in range(1,m1):
        tmp1 += num_of_days[i]
    tmp1 +=d1
    for i in range(1,m2):
        tmp2 += num_of_days[i]
    tmp2 += d2
    return tmp2 - tmp1
m1,d1,m2,d2 = map(int,input().split())
day=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun' ]
print(day[cnt_day(m1,d1,m2,d2)%7])