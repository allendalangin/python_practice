def add(a, b=5):
    return a + b

def is_palindrome(str):
    return str == str[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) 

print(add(10))
print(add(10,20))

print(is_palindrome("racecar"))

print(factorial(10))