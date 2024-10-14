import random

# # Create List1 with 20 random numbers between 1 and 10
# List1 = [random.randint(1, 10) for _ in range(20)]

# Create List2 to count occurrences of numbers 1 through 10
# List2 = [List1.count(i) for i in range(1, 11)]

# Display both lists
# print("List1:", List1)
# print("List2 (Frequency of numbers 1 to 10):", List2)



# Step 1: Define a list (you can change the list to anything you like)
original_list = [1, 2, 3, 4, 5,6,7,8,9]

# Step 2: Rotate the list so the last element moves to the first position
rotated_list = [original_list[-1]] + original_list[:-1]
# rotated_list.append(original_list[-1])
# for i in range(len(original_list)-1):
#     rotated_list.append(original_list[i])

# Step 3: Display the original and rotated lists
# print("Original List:", original_list)
# print("Rotated List:", rotated_list)
u='2'*'2'
print(u)