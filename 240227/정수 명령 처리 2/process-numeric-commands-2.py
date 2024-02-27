from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    def push(self,item):
        self.dq.append(item)

    def empty(self):
        return not self.dq
    def size(self):
        return len(self.dq)
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()
    def front(self):
        if self.empty():
            raise Exception ("Queue is empty")
        return self.dq[0]

n = int(input())
arr= Queue()
for _ in range(n):
    tmp = input().split()
    if tmp[0] == 'push':
        arr.push(int(tmp[1]))
    elif tmp[0] == 'pop':
        print(arr.pop())
    elif tmp[0] == 'size':
        print(arr.size())
    elif tmp[0] == 'empty':
        print(1 if arr.empty() == True else 0)
    elif tmp[0] == 'front':
        print(arr.front())