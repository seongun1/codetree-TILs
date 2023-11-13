arr=["apple", "banana", "grape", "blueberry", "orange"]
str = input()
cnt =0
for a in arr:
    if a[2] == str or a[3] == str:
        cnt +=1
        print(a)
print(cnt)