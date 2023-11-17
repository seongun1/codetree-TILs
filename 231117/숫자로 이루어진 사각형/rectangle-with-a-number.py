n=int(input())
def draw_rec(n):
    cnt =1
    for i in range(n):
        for j in range(n):
            if cnt ==10:
                cnt =1
            print(cnt,end=' ')
            cnt +=1
        print()
draw_rec(n)