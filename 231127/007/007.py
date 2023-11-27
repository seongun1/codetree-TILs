class secret:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time
tmp = input().split()
tmp = secret(tmp[0],tmp[1],tmp[2])
print(f"secret code : {tmp.code}")
print(f"meeting point : {tmp.place}")
print(f"time : {tmp.time}")