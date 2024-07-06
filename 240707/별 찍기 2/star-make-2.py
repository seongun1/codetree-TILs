a,b = map(int,input().split())
#a는 별 모양의 크기, b 는 별 모양의 종류

if b ==1:
    for star in range(1,a//2+2):
        for _ in range(star):
            print('*',end='')
        print()
    for star in range(a//2,0,-1):
        for _ in range(star):
            print('*',end='')
        print()
elif b ==2:
    for star in range(1,a//2+2):
        blank = (a//2+1) - star
        for _ in range (blank): print(' ',end='')
        for _ in range(star) : print('*',end='')
        print()
    for star in range(a//2,0,-1):
        blank = a //2 +1 - star
        for _ in range(blank):
            print(' ',end='')
        for _ in range(star):
            print('*',end='')
        print()
elif b ==3:
    blank = 0
    for star in range(a,-1,-2):
        for _ in range(blank):
            print(' ',end='')
        for _ in range(star):
            print('*',end='')
        blank +=1
        print()
    blank-=1
    for star in range(3,a+1,2):
        blank -=1
        for _ in range(blank):
            print(' ',end='')
        for _ in range(star):
            print('*',end='')
        print()
elif b ==4:
    half = a //2 +1
    blank = 0
    for star in range(half,0,-1):
        for _ in range(blank):
            print(' ',end='')
        for _ in range(star):
            print('*',end='')
        print()
        blank +=1
    blank -=1
    for star in range(2,half+1):
        for _ in range(blank):
            print(' ',end='')
        for _ in range(star):
            print('*',end='')
        print()