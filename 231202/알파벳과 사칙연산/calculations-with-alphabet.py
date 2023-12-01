string = input()
length = len(string)

operand = list()
for i in string:
    if i in ['+','-','*']:
        operand.append(i)

ans = []
max_val = 0

def println():
    global max_val

    cnt = ans[0]
    for i in range(len(ans)-1):
        temp = ''
        temp += str(cnt)
        temp += operand[i]
        temp += str(ans[i+1])
        
        cnt = eval(temp) 
    
    max_val = max(max_val, cnt)


def choose(cur):
    if cur == length //2 + 1:
        println()
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cur+1)
        ans.pop()
    return 

choose(0)
print(max_val)