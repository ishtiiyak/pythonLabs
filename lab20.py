import sys
from timeit import timeit

# 1. Tuple basics
print("1. Tuple Basics:")
a = (2, 3, 6, False, 'Lecture')
print("Tuple a:", a)

# Indexing
print("Accessing element at index 3:", a[3])   # False
print("Accessing last element:", a[-1])        # 'Lecture'

# Membership
print("Is 3 in tuple a?", 3 in a)              # True

# Slicing
print("Slicing tuple from index 1 to 4:", a[1:4])  # (3, 6, False)
print("\n")

# 2. Comparison between List and Tuple (Memory and Execution Time)
print("2. Memory Comparison between List and Tuple:")
list_a = [4, 5, 9.2, 'Computer', True]
tuple_a = (4, 5, 9.2, 'Computer', True)

print("Size of list:", sys.getsizeof(list_a))    # Memory size of list
print("Size of tuple:", sys.getsizeof(tuple_a))  # Memory size of tuple

# Time comparison
print("\nExecution time for creating List and Tuple (100 Million times):")
list_time = timeit(stmt='[1,2,3,4,5]', number=100_000_000)
tuple_time = timeit(stmt='(1,2,3,4,5)', number=100_000_000)
print(f'List creation time: {list_time}')
print(f'Tuple creation time: {tuple_time}')
print("\n")

# 3. Tuple Operations
print("3. Tuple Operations:")
b = (2, 4, 1)

# Concatenation
c = a + b
print("Concatenated tuple:", c)

# Repetition
print("Repeated tuple:", b * 2)

# Comparison
print("Are tuples a and b equal?", a == b)    # False
print("Is tuple a greater than b?", a > b)    # False (based on element comparison)

# Built-in functions
print("Length of tuple b:", len(b))           # 3
print("Maximum value in tuple b:", max(b))    # 4
print("Minimum value in tuple b:", min(b))    # 1
print("Sum of elements in tuple b:", sum(b))  # 7
print("Is all elements of tuple b True?", all(b))  # True
print("Is any element of tuple b True?", any(b))  # True
print("\n")

# 4. Tuple immutability vs List mutability
print("4. Tuple Immutability vs List Mutability:")
# List can be changed (mutable)
list_b = [2, 3, 10]
list_b[0] = 5
print("Modified list:", list_b)  # [5, 3, 10]

# Tuple cannot be changed (immutable)
try:
    tuple_b = (2, 3, 10)
    tuple_b[0] = 5  # This will raise an error
except TypeError as e:
    print("Error while modifying tuple:", e)
print("\n")

# 5. Packing and Unpacking of Tuples
print("5. Packing and Unpacking Tuples:")
# Packing
packed_tuple = 3, 4, 5
print("Packed tuple:", packed_tuple)

# Unpacking
a, b, c = packed_tuple
print(f"Unpacked values: a={a}, b={b}, c={c}")

# Unpacking with *
packed_tuple = 3, 4, 5, 6, 7, 8, 9
a, b, *c = packed_tuple
print(f"Unpacked with *: a={a}, b={b}, c={c}")
print("\n")

# 6. Tuple as Function Return Values
print("6. Tuple as Function Return Values:")
def test(a, b):
    return a + b, a - b  # Returns a tuple

sum_value, diff_value = test(10, 2)
print(f"Sum: {sum_value}, Difference: {diff_value}")
print("\n")

# 7. Singleton Tuple
print("7. Singleton Tuple:")
t1 = (1,)  # Note the comma
print(f"Singleton tuple: {t1}, Type: {type(t1)}")
print("\n")

# 8. Tuple Use Case Example: Zodiac Sign Calculation
print("8. Zodiac Sign Example Using Tuple:")

def zodiac(day, month):
    signs = (
        ('Capricorn', 19), ('Aquarius', 18), ('Pisces', 20),
        ('Aries', 19), ('Taurus', 20), ('Gemini', 20),
        ('Cancer', 22), ('Leo', 22), ('Virgo', 22),
        ('Libra', 22), ('Scorpio', 21), ('Sagittarius', 21),
        ('Capricorn', )
    )
    if day <= signs[month - 1][1]:
        return signs[month - 1][0]
    else:
        return signs[month][0]

print("Zodiac sign for 15th July:", zodiac(15, 7))  # Cancer
print("Zodiac sign for 25th July:", zodiac(25, 7))  # Leo
