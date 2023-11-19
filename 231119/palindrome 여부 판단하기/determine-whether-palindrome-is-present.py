a= input()
def is_palindrome(string):
    if string == string[::-1]:
        return 'Yes'
    else:
        return 'No'
print(is_palindrome(a))