string= input()
print(string)
for i in range(len(string)):
    string = string[-1] + string[:-1]
    print(string)