################################ Assesment last  ########################################

def factorial(n):
    if n < 0:
        return "Input should be a non-negative integer"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage
n = 5
print(f"Factorial of {n} is {factorial(n)}")
def fibonacci(n):
    def cubical_root(n):
        if n < 0:
            return -(-n) ** (1/3)
        else:
            return n ** (1/3)

    # Example usage
    n = 27
    print(f"Cubical root of {n} is {cubical_root(n)}")
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Example usage
n = 10
print(f"Fibonacci number at position {n} is {fibonacci(n)}")