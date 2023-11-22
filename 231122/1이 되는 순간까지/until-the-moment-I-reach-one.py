n=int(input())

def num_val(n,cnt):
    if n==1:
        print(cnt)
        return
    if not n%2:
        n //=2
        cnt +=1
        return num_val(n,cnt)
    else:
        n//=3       
        cnt +=1 
        return num_val(n,cnt)
num_val(n,0)