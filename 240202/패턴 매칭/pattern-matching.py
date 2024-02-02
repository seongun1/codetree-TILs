import sys

s = input()
p = input()

n = len(s)
m = len(p)


def possible():
    for i in range(1,n+1):
        #print("s[i-1] : {}, p[i-1]] : {}".format(s[i-1], p[i-1]))
        if (s[i-1] == p[i-1]) or (p[i-1] == '.'):
            continue
        elif (p[i-1] == '*') :
            return True
        else:
            return False
    return True

if possible():
    print("true")
else:
    print("false")