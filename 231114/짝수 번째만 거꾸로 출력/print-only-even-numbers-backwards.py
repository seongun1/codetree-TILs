string = input()
string = string[::-1]
for i in range(0,len(string),2):
    print(string[i],end='')