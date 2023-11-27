class bomb:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second
tmp = tuple(input().split())
tmp = bomb(tmp[0],tmp[1],tmp[2])

print(f"code : {tmp.code}")
print(f"color : {tmp.color}")
print(f"second : {tmp.second}")