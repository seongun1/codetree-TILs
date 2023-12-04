m1,d1,m2,d2=tuple(map(int,input().split()))
A = str(input())

# m1,d1,m2,d2 = 12, 14, 12, 29
# A = 'Fri'

# m1, d1, m2, d2 = 2, 5, 3, 9
# A = 'Mon'

# m1, d1, m2, d2 = 12, 11, 12, 20
# A = 'Thu'

day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
idx = 0

for i in range(len(day)) :
    if A == day[i] :
        idx = i

def total_days(m,d):
    nums_of_day =[0,31,29,31,30,31,30,31,31,30,31,30,31]
    total_days = d

    for i in range(1, m) :
        total_days += nums_of_day[i]

    return total_days

diff = total_days(m2, d2) - total_days(m1, d1) + 1
cnt = 0
week_of_day = 0

for i in range(1, diff + 1) :
    week_of_day = (week_of_day + 1) % 7

    if day[week_of_day - 1] == A : 
        cnt += 1
print(cnt)