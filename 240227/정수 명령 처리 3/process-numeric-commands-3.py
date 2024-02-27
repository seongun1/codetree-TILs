from collections import deque
arr= deque()
n = int(input())
for _ in range(n):
    tmp = input().split()

    if tmp[0] == 'push_front':
        arr.appendleft(int(tmp[1]))
    elif tmp[0] == 'push_back':
        arr.append(int(tmp[1]))
    elif tmp[0] == 'pop_front':
        print(arr.popleft())
    elif tmp[0] == 'pop_back':
        print(arr.pop())
    elif tmp[0] == 'size':
        print(len(arr))
    elif tmp[0] == 'empty':
        print(1 if not arr else 0)
    elif tmp[0] == 'front':
        print(arr[0])
    elif tmp[0] == 'back':
        print(arr[-1])