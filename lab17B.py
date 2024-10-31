import random

# # Create List1 with 20 random numbers between 1 and 10
# List1 = [random.randint(1, 10) for _ in range(20)]

# Create List2 to count occurrences of numbers 1 through 10
# List2 = [List1.count(i) for i in range(1, 11)]

# Display both lists
# print("List1:", List1)
# print("List2 (Frequency of numbers 1 to 10):", List2)



# Step 1: Define a list (you can change the list to anything you like)
# original_list = [1, 2, 3, 4, 5,6,7,8,9]

# Step 2: Rotate the list so the last element moves to the first position
# rotated_list = [original_list[-1]] + original_list[:-1]
# rotated_list.append(original_list[-1])
# for i in range(len(original_list)-1):
#     rotated_list.append(original_list[i])

# Step 3: Display the original and rotated lists
# print("Original List:", original_list)
# print("Rotated List:", rotated_list)
# u='2'*'2'
# print(u)

# List of numbers
numbers = [61.5, 59, 56, 54.5, 54.5, 54, 53, 50, 49.5, 
           48.5, 47, 46, 45.5, 44, 41.5, 40.5, 40, 40, 
           37.5, 36.5, 36, 36, 35, 35, 34.5, 34.5, 34, 
           34, 33.5, 33, 32.5, 32, 31.5, 31, 31, 30.5, 
           30.5, 30.5, 29, 29, 27, 26.5, 26, 25.5, 24.5, 
           24.5, 23.5, 23.5, 22.5, 22.5, 22, 22, 21.5, 20.5, 
           18.5, 17.5, 16.5, 16.5, 14.5, 14, 14, 12, 9.5, 8.5]

# Sorting the list
sorted_numbers = sorted(numbers,reverse=True)

# Printing the sorted list
print(sorted_numbers,len(numbers))
