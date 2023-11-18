a,b =map(int,input().split())
cnt =0
def is_369(i):
    i = str(i)
    return '3' in i or '6' in i or '9' in i

def is_countable(i):
    return not i%3 or is_369(i)

for i in range(a,b+1):
    if is_countable(i):
        cnt +=1

print(cnt)