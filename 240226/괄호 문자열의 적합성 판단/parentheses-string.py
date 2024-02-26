tmp = input()
tmp = list(tmp)
arr= []
def is_correct():
    for i in range(len(tmp)):
        if tmp[i] == '(':
            arr.append(tmp[i])
        elif tmp[i] ==')':
            if len(arr) == 0 or arr[-1] == ')':
                return 'No'
            arr.pop()
    if len(arr) ==0:
        return 'Yes'
    return 'No'
print(is_correct())