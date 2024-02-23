n = int(input())
arr= list(map(int,input().split()))


def partition(low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i +=1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1], arr[high] = arr[high],arr[i+1]

    return i+1

def quick(low,high):
    if low < high: #원소의 갯수가 2개 이상일 때
        pos = partition(low,high)
        quick(low,pos-1)
        quick(pos,high)

quick(0,n-1)
for a in arr:
    print(a,end=' ')