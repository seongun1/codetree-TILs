n = int(input())

d = [0] * 1001

d[0] = 1
d[1] = 2
d[2] = 7


for i in range(3,n+1):
    d[i] = (d[i-1] * 3) + d[i-2] - d[i-3]
print(d[n] % 1000000007)

#2 -> 7 -> 22 -> 71