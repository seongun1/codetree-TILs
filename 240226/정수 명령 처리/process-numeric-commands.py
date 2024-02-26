class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]


n= int(input())

s = stack()
for _ in range(n):
    tmp = list(input().split())
    if tmp[0] == 'push':
        s.push(int(tmp[1]))
    elif tmp[0] == 'size':
        print(s.size())
    elif tmp[0] == 'empty':
        print(0 if s.empty() == False else 1)
    elif tmp[0] =='pop':
        print(s.pop())
    elif tmp[0] == 'top':
        print(s.top())