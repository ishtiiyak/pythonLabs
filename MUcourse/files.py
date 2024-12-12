fhandle = open(r'C:\Users\BUZZ TECH\pythonLabs\MUcourse\txt\files.txt', 'r')
for line in fhandle:
    #line=line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)

def fibonacci(n):
    # Initialize first two numbers in series
    a, b = 0, 1
    # Print first n numbers in series
    for i in range(n):
        print(a, end=' ')
        # Calculate next number and update values
        a, b = b, a + b
    print() # New line at end

# Test the function
fibonacci(10) # Prints first 10 numbers in Fibonacci series





def factorial(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n-1)

print(factorial(5))


