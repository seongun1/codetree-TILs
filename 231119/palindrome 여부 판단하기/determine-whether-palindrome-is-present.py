a= input()
def is_palindrome(string):
    a = string[::-1]
    for i in range(len(string)):
        if string[i] != a[i]:
            return 'No'
    return 'Yes'
print(is_palindrome(a))