string = input()
tmp =''
for i in range(len(string)):
    if i%2:
        tmp +=string[i]
tmp = tmp[::-1]
print(tmp)