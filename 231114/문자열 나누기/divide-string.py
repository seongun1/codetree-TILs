n=int(input())
tmp =input()
arr="".join(tmp.split())

for i in range(len(arr)):
    if not i%5 and i !=0:
        print()
    print(arr[i],end='')