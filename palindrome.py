# You can pass any type of parameter to check whether it's palindrome or not

def is_palindrome(string):
    string = str(string)
    return string == string[len(string)::-1]


