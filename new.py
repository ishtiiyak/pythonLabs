# --------------------------------- STRINGS ---------------------------------
print("=== Strings ===")

# Strings are immutable sequences of characters. Once a string is created, it cannot be modified.
# You can create a string using single or double quotes.

string1 = "Hello, Python!"  # Using double quotes
string2 = 'Welcome to Python programming'  # Using single quotes

# Accessing individual characters (indexing starts from 0)
print(string1[0])  # Output: H
print(string2[-1])  # Output: g (negative index starts from the end)

# Strings are immutable; you cannot change individual characters directly
# string1[0] = 'h'  # This will raise an error

# String slicing: Extracting parts of a string
print(string1[0:5])  # Output: Hello
print(string1[7:])   # Output: Python!

# Concatenation: Joining strings
greeting = "Hello"
name = "John"
print(greeting + ", " + name)  # Output: Hello, John

# String length
print(len(string1))  # Output: 13

# String methods
# upper() and lower() change case
print(greeting.upper())  # Output: HELLO
print(greeting.lower())  # Output: hello

# replace() substitutes parts of a string
print(string1.replace("Python", "World"))  # Output: Hello, World!

# find() returns the first occurrence of a substring
index = string1.find("Python")
print(index)  # Output: 7

# split() splits a string into a list of substrings
words = string2.split()  # Default delimiter is any whitespace
print(words)  # Output: ['Welcome', 'to', 'Python', 'programming']

# join() joins a list of strings into a single string
sentence = ' '.join(words)
print(sentence)  # Output: Welcome to Python programming

# strip() removes leading and trailing whitespace
extra_space_str = "  Hello, Python!  "
print(extra_space_str.strip())  # Output: "Hello, Python!"

# String formatting using f-strings (Python 3.6+)
age = 25
formatted_str = f"{name} is {age} years old."
print(formatted_str)  # Output: John is 25 years old.

# ----------------------------- SETS -----------------------------
print("\n=== Sets ===")

# A set is an unordered collection of unique elements. Duplicates are automatically removed.
my_set = {1, 2, 3, 4, 4}  # Duplicates will be removed
print(my_set)  # Output: {1, 2, 3, 4}

# Sets support basic operations like adding and removing elements.
# Adding elements to a set
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing elements from a set
my_set.remove(2)  # Raises an error if element not found
print(my_set)  # Output: {1, 3, 4, 5}

# discard() removes an element, but does not raise an error if the element is missing
my_set.discard(10)  # No error

# Set operations: Union, Intersection, Difference, Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: Elements present in either set
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection: Elements common to both sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference: Elements in set1 but not in set2
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Symmetric difference: Elements in either set, but not in both
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# Checking if an element exists in a set
print(3 in set1)  # Output: True
print(10 in set1)  # Output: False

# Sets are mutable, but elements must be immutable (e.g., numbers, strings, tuples)
# my_set = {[1, 2], 3}  # This will raise a TypeError because lists are mutable

# ----------------------------- DICTIONARIES -----------------------------
print("\n=== Dictionaries ===")

# Dictionaries store data as key-value pairs.
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values via keys
print(person["name"])  # Output: John

# Modifying a value
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
person["profession"] = "Engineer"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'profession': 'Engineer'}

# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'profession': 'Engineer'}

# Dictionary methods: keys(), values(), items()
print(person.keys())   # Output: dict_keys(['name', 'age', 'profession'])
print(person.values())  # Output: dict_values(['John', 31, 'Engineer'])
print(person.items())   # Output: dict_items([('name', 'John'), ('age', 31), ('profession', 'Engineer')])

# Checking if a key exists in the dictionary
print("name" in person)  # Output: True

# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# ----------------------------- FILE READ AND WRITE -----------------------------
print("\n=== File Read and Write ===")

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, Python!\nThis is a sample file.")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading a file line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\nThis is an appended line.")

# ----------------------------- EXCEPTION HANDLING -----------------------------
print("\n=== Exception Handling ===")

#           
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Handling multiple exceptions
try:
    num = int(input("Enter a number: "))  # Could raise ValueError
    result = 10 / num                     # Could raise ZeroDivisionError
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Using finally block to ensure execution
try:
    file = open("example.txt", 'r')
    content = file.read()
finally:
    file.close()  # Ensures the file is closed, even if an error occurs

# Raising custom exceptions
def check_positive_number(n):
    if n <= 0:
        raise ValueError("The number must be positive!")
    return n

try:
    check_positive_number(-5)
except ValueError as e:
    print(e)  # Output: The number must be positive!

# ----------------------------- POSITIONAL & KEYWORD ARGUMENTS -----------------------------
print("\n=== Positional & Keyword Arguments ===")

# Positional arguments are passed in the order defined, while keyword arguments are passed by name.

def greet(first_name, last_name, greeting="Hello"):
    print(f"{greeting}, {first_name} {last_name}!")

# Positional arguments
greet("John", "Doe")  # Output: Hello, John Doe!

# Keyword arguments
greet(first_name="Jane", last_name="Smith", greeting="Hi")  # Output: Hi, Jane Smith!

# Default argument
greet("Alice", "Brown")  # Output: Hello, Alice Brown!

# Variable-length arguments: *args and **kwargs
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, "hello")  # Output: 1, 2, 3, hello

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John", age=25)  # Output: name: John, age: 25

# ----------------------------- RECURSION & MEMOIZATION -----------------------------
print("\n=== Recursion & Memoization ===")

# Recursion is when a function calls itself. It is often used to solve problems that can be broken down into smaller subproblems.

# Example: Calculating factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

# Recursive Fibonacci without memoization (inefficient)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55

# Memoization: Caching the results of expensive function calls and reusing them
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

print(fibonacci_memo(10))  # Output: 55 (much faster with memoization)







def word_frequency_analyzer(text, exclude_words=None, top_n=5, case_sensitive=False):
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")
    if not isinstance(top_n, int) or top_n <= 0:
        raise ValueError("top_n must be a positive integer.")
    if exclude_words is None:
        exclude_words = set()
    elif not isinstance(exclude_words, set):
        raise ValueError("exclude_words must be a set.")
    def count_words_recursive(text, memo={}):
        if text in memo:
            return memo[text]
        words = ''.join([c if c.isalnum() else ' ' for c in text]).split()
        word_count = {}
        for word in words:
            if not case_sensitive:
                word = word.lower()
            if word not in exclude_words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        memo[text] = word_count
        return word_count
    word_count = count_words_recursive(text)
    sorted_words = sort_by_frequency(word_count)
    return sorted_words[:top_n]
def sort_by_frequency(word_count):
    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)










import re
from collections import Counter

# ------------------ 1. Sentence Analyzer ------------------
def sentence_analyzer(text):
    """Counts the total number of words and sentences in a given text."""
    clean_text = re.sub(r'[;,:]', '', text)  # Remove commas and semicolons
    words = clean_text.split()  # Split by spaces to count words
    sentences = re.split(r'[.!?]', clean_text)  # Split by '.', '!', '?'
    sentences = [s for s in sentences if s.strip()]  # Remove empty sentences
    return len(words), len(sentences)

# ------------------ 2. Anagram Checker ------------------
def is_anagram(str1, str2):
    """Checks if two strings are anagrams, ignoring case and spaces."""
    str1 = ''.join(str1.lower().split())  # Normalize strings
    str2 = ''.join(str2.lower().split())
    return sorted(str1) == sorted(str2)

# ------------------ 3. Palindrome Checker ------------------
def is_palindrome(s):
    """Checks if the given string is a palindrome."""
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Remove non-alphanumeric chars and convert to lowercase
    return s == s[::-1]

# ------------------ 4. Character Frequency Counter ------------------
def char_frequency(text):
    """Counts the frequency of each character in the text."""
    frequency = {}
    for char in text:
        if char.isalnum():  # Count only alphanumeric characters
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

# ------------------ 5. Word Frequency Counter ------------------
def word_frequency_analyzer(text, exclude_words=None, top_n=5, case_sensitive=False):
    """Analyzes word frequency in the text, optionally excluding certain words."""
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")
    if not isinstance(top_n, int) or top_n <= 0:
        raise ValueError("top_n must be a positive integer.")
    if exclude_words is None:
        exclude_words = set()
    elif not isinstance(exclude_words, set):
        raise ValueError("exclude_words must be a set.")
    def count_words_recursive(text, memo={}):
        if text in memo:
            return memo[text]
        words = ''.join([c if c.isalnum() else ' ' for c in text]).split()
        word_count = {}
        for word in words:
            if not case_sensitive:
                word = word.lower()
            if word not in exclude_words:
                word_count[word] = word_count.get(word, 0) + 1
        memo[text] = word_count
        return word_count
    word_count = count_words_recursive(text)
    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:top_n]

# ------------------ 6. Fibonacci Sequence Generator ------------------
def fibonacci(n):
    """Generates the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# ------------------ 7. Prime Number Checker ------------------
def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ------------------ 8. Factorial Calculator ------------------
def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# ------------------ 9. Recursive Reverse String ------------------
def reverse_string(s):
    """Reverses a string recursively."""
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])

# ------------------ 10. Find Common Elements in Two Lists ------------------
def find_common_elements(list1, list2):
    """Finds common elements between two lists."""
    return list(set(list1) & set(list2))

# ------------------ Testing All Functions ------------------
if __name__ == "__main__":
    # Test 1: Sentence Analyzer
    text = "Hello! How are you doing today? I'm fine. Let's go out."
    print("Sentence Analyzer:", sentence_analyzer(text))

    # Test 2: Anagram Checker
    print("Anagram Test (Listen, Silent):", is_anagram("Listen", "Silent"))
    print("Anagram Test (Hello, World):", is_anagram("Hello", "World"))

    # Test 3: Palindrome Checker
    print("Palindrome Test (A man, a plan, a canal, Panama):", is_palindrome("A man, a plan, a canal, Panama"))
    print("Palindrome Test (Hello):", is_palindrome("Hello"))

    # Test 4: Character Frequency
    text = "Hello, Python!"
    print("Character Frequency:", char_frequency(text))

    # Test 5: Word Frequency Analyzer
    text = "Hello, hello, Python! This is a Python test. Python is great!"
    exclude = {"is"}
    print("Word Frequency:", word_frequency_analyzer(text, exclude_words=exclude, top_n=3))

    # Test 6: Fibonacci Sequence
    print("Fibonacci (first 10 terms):", fibonacci(10))

    # Test 7: Prime Number Checker
    print("Prime Test (7):", is_prime(7))
    print("Prime Test (15):", is_prime(15))

    # Test 8: Factorial
    print("Factorial (5):", factorial(5))

    # Test 9: Reverse String
    print("Reverse String (Python):", reverse_string("Python"))

    # Test 10: Find Common Elements in Lists
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print("Common Elements:", find_common_elements(list1, list2))
