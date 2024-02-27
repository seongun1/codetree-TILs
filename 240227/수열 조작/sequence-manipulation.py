from collections import deque
dq = deque()
n = int(input())

for i in range(1,n+1):
    dq.append(i)
while len(dq) != 1:
    dq.popleft()
    val = dq.popleft()
    dq.append(val)
print(dq[0])