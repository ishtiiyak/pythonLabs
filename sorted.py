

# Initial list of numbers
numbers = [2.1, 2.7, 2.20, 2.21, 2.24, 2.25, 2.26, 2.28, 2.33, 2.44, 2.48, 2.49, 2.50, 2.51, 2.52,
           2.1,2.2,2.3,2.4,2.6,2.37,2.5, 2.17,2.38, 2.39, 2.40,2.41,
           2.9, 2.10, 2.13, 2.14, 2.30, 2.31, 2.34, 2.35, 2.36,
           2.15, 2.22, 2.23, 2.29, 2.32, 2.42, 2.43,2.11,2.12]

# Custom sorting function
def custom_sort_key(num):
    # Split the number into integer and fractional parts
    integer_part, fractional_part = str(num).split('.')
    return (int(integer_part), int(fractional_part))

# Sorting using the custom key function
numbers.sort(key=custom_sort_key)

# Printing the sorted list
print(numbers)

[2.1, 2.1, 2.1, 2.2, 2.2, 2.3, 2.3, 2.4, 2.4, 2.5, 2.5,
  2.6, 2.7, 2.9, 2.11, 2.12, 2.13, 2.14, 2.15, 2.17, 2.21,
    2.22, 2.23, 2.24, 2.25, 2.26, 2.28, 2.29, 2.31, 2.32,
    2.33, 2.34, 2.35, 2.36, 2.37, 2.38, 2.39, 2.41, 2.42,
    2.43, 2.44, 2.48, 2.49, 2.51, 2.52]