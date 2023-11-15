s,q=input().split()
s =list(s)
q=int(q)
for i in range(q):
    t,a,b=input().split()
    if t =='1':
        a = int(a)
        b=int(b)
        s[a-1],s[b-1] = s[b-1],s[a-1]
        print(''.join(s))
    elif t == '2':
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        print(''.join(s))