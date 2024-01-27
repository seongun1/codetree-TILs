n = int(input())

d = [0] * 1001

d[0] = 0
d[1] = 2
d[2] = 7


for i in range(3,n+1):
    d[i] = (d[i-1] * 3 + 1) % 1000000007
print(d[n])