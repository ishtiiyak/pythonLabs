fhandle = open(r'C:\Users\BUZZ TECH\pythonLabs\MUcourse\txt\files.txt', 'r

for line in fhandle:
    #line=line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)

def fibonacci(n):
    """
    Generate first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Raises:
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
        
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def factorial(n):
    """
    Calculate the factorial of n.
    
    Args:
        n (int): Number to calculate factorial for
        
    Returns:
        int: n!
        
    Raises:
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
        
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Test cases
try:
    fibonacci(10)
    print(factorial(5))
except (ValueError, TypeError) as e:
    print(f"Error: {e}")


