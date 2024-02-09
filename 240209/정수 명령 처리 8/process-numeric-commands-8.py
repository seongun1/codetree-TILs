class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self,new_data): #가장 앞으로 넣는 함수.
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head !=None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else: #기존 리스트 비어있을 경우
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num +=1
    
    def push_back(self,new_data): #가장 뒤에 넣는 함수
        new_node = Node(new_data)
        new_node.prev = self.tail
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        self.node_num +=1

    def pop_front (self): #첫번째 수를 빼기
        if self.head ==None:
            print("List is empty")

        elif self.head.next == None:
            tmp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return tmp.data
        
        else:
            tmp = self.head
            tmp.next.prev = None
            self.head = tmp.next
            tmp.next = None

            self.node_num -=1
            return tmp.data

    def pop_back(self):
        if self.tail == None:
            print("List is empty")
        elif self.tail.prev == None:
            tmp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return tmp.data

        else:
            tmp = self.tail
            tmp.prev.next = None
            self.tail = tmp.prev
            tmp.prev = None
            self.node_num -= 1
            return tmp.data

    def size(self):
        return self.node_num

    def empty(self):
        if self.node_num == 0:
            return 1
        else:
            return 0
    def front(self):
        if self.head ==None:
            print("List is empty")
        else:
            return self.head.data

    def back (self):
        if self.tail == None:
            print("List is empty")

        else:
            return self.tail.data


n = int(input())
L = DLL()
for _ in range(n):
    tmp = input().split()
    if tmp[0] == 'push_back':
        L.push_back(int(tmp[1]))
    elif tmp[0] == 'push_front':
        L.push_front(int(tmp[1]))

    elif tmp[0] == 'pop_front':
        print(L.pop_front())
    elif tmp[0] == 'pop_back':
        print(L.pop_back())

    elif tmp[0] == 'front':
        print(L.front())
    elif tmp[0] == 'back':
        print(L.back())
    elif tmp[0] == 'size':
        print(L.size())
    elif tmp[0] == 'empty':
        print(L.empty())