# A function to calculate the factorial of the input parameter value using recursion
def factorial(n):
    if n < 0:
        return None # There is no factorial of negative integers 
    elif n == 0 or n == 1:
        return 1 # 0! == 1 && 1! == 1
    else:
        return n * factorial(n - 1) # Recursion call


# A function to calculate 'n'th fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        return None # No fibonacci number for negative values
    elif n == 1 or n == 2:
        return 1 # 1st and 2nd fibonacci numbers are 1. The sequence: 1,1,2,3,5,8....
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Recursion call


# A function to calculate sum of 'n' natural numbers
def sum(n):
    if n < 0:
        return None # To avoid RecursionError
    if n == 1 or n == 0:
        return n
    else:
        return n + sum(n - 1) # Recursion call

print(sum(-1))