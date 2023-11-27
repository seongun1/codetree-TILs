class id_level:
    def __init__(self,id,level):
        self.id = id
        self.level = level

tmp1 = id_level("codetree",10)
tmp2 = input().split()
tmp2  = id_level(tmp2[0],tmp2[1])
print(f"user {tmp1.id} lv {tmp1.level}")
print(f"user {tmp2.id} lv {tmp2.level}")