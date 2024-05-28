n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
#print(arr)
box1_num = -9999
box2_num = -9999

ans = -9999

def find_answer(i,j,i2,j2,w1,w2,h1,h2):
    tmp_box1,tmp_box2 = 0,0
    for x in range(i,i+w1+1):
        for y in range(j,j+h1+1):
            tmp_box1 += arr[x][y]
    for x in range(i2,i2+w2+1):
        for y in range(j2,j2+h2+1):
            tmp_box2 += arr[x][y]
    return tmp_box1,tmp_box2

    
for i in range(n):
    for j in range(m):
        for w1 in range(n):
            for h1 in range(m):
                if i+w1 >=n or j+h1>=m:
                    continue
                for i2 in range(n):
                    for j2 in range(m):
                        for w2 in range(n):
                            for h2 in range(m):
                                if i2 +w2 >=n or j2 +h2>=m:
                                    continue
                                if (i+w1 < i2 or j + h1 < j2) :
                                    #print(i,w1,i2,w2,j,h1,j2,h2)
                                    tmp_box1,tmp_box2 =find_answer(i,j,i2,j2,w1,w2,h1,h2)
                                    ans = max(ans,tmp_box1+tmp_box2)

print(ans)