from collections import deque

n = int(input())

q = deque()
q.append((n))
res = 0

while q:
    val = q.popleft()

    if val == 1:
        break

    if val % 3 == 0:
        val //= 3
    elif val % 2 == 0:
        val //= 2
    elif (val + 1) % 2 == 0 or (val + 1) % 3 == 0:
        val += 1
    elif (val - 1) % 2 == 0 or (val - 1) % 3 == 0:
        val -= 1
    else:
        val -= 1
    
    res += 1
    q.append(val)

print(res)