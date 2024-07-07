tmp = input()
tmp = list(tmp)
def is_correct(tmp):
    a,b = 0,0
    for t in tmp:
        if t =='(':
            a +=1
        else:
            b+=1
    return a ==b

cnt =0

for i in range(len(tmp)): #하나씩 변경
    if tmp[i] == '(':
        tmp[i] = ')'
    else:
        tmp[i] = '('
    #print(tmp)
    if not is_correct(tmp):
        if tmp[i] == '(': tmp[i] =')'
        else: tmp[i] ='('
        continue
    a,b = 0,0
    success = True
    for j in range(len(tmp)):
        if tmp[j] == '(':
            a +=1
        else:
            b +=1
        if a <b:
            success = False
            break
    if success:
        cnt +=1
    if tmp[i] == '(': tmp[i] =')'
    else: tmp[i] = '('
print(cnt)