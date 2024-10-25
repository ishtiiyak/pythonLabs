# # with open('email.txt', 'w') as file:
# #     file.write("Please contact ali.hassan@gmail.com ali@gmail.com for assistance.")
# # with open('email.txt', 'w') as file:
# #     red=file.read()
# def extract_emails(text):
#     words = text.split()
#     emails = [word for word in words if '@' in word]
#     return emails

# def mask_emails(emails):
#     masked_emails = []
#     for email in emails:
#         index = email.find('@')
#         masked_email = '*' * index + email[index:]
#         masked_emails.append(masked_email)
#     return masked_emails


# string = "Please contact  ali.hassan@gmail.com ali@gmail.com for assistance."
# filename = 'email.txt'

# emails = extract_emails(string)
# masked_emails = mask_emails(emails)

# print(masked_emails)


# Memoization using a dictionary
fib_cache = {}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 1 or n == 2:
        value = 1
    else:
        value = fib(n - 1) + fib(n - 2)
    # print(value)
    # Store the computed value in cache
    fib_cache[n] = value
    # print(fib_cache.values())
    return value


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(235))  # Output: 120

# print(fib(10))  # Output: 55


def fibonacci(n):
    if n <= 1:
        return n
    else:
        print(n,end=' ')
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example: Find the 10th Fibonacci number
print(fibonacci(100))  # Output: 55

