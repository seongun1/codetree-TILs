n= int(input())
arr =list(map(int,input().split()))
def radix_sort(arr):
    max_num = max(arr)
    max_digit = len(str(max_num))

    for digit in range(max_digit):
        buckets= [[] for _ in range(10)]

        for num in arr:
            digit_val = (num // (10**digit)) %10
            buckets[digit_val].append(num)
        arr = [num for bucket in buckets for num in bucket]

    return arr

arr = radix_sort(arr)
for a in arr:
    print(a,end=' ')