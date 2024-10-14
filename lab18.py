def process_values(lst):
    # Calculate average
    avg = sum(lst) / len(lst)
    
    less_than_avg = []
    equal_to_avg = []
    greater_than_avg = []
    
    # Separate values based on their relation to the average
    for value in lst:
        if value < avg:
            less_than_avg.append(value)
        elif value == avg:
            equal_to_avg.append(value)
        else:
            greater_than_avg.append(value)
    
    return less_than_avg, equal_to_avg, greater_than_avg

def get_user_input():
    user_values = []
    
    while True:
        user_input = input("Enter a number (or press enter to stop): ")
        
        if user_input == '':
            break  # Exit loop on blank input
        try:
            # Convert input to float and append to list
            num = float(user_input)
            user_values.append(num)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    return user_values

# Get user input
values = get_user_input()

# If user provided any values, process them
if values:
    less_than_avg, equal_to_avg, greater_than_avg = process_values(values)

    # Display the results
    print("\nValues less than the average:", less_than_avg)
    print("Values equal to the average:", equal_to_avg)
    print("Values greater than the average:", greater_than_avg)
else:
    print("No values were entered.")








def isSorted(lst):
    # Check if the list is sorted in non-decreasing order
    return lst == sorted(lst)

def get_user_input():
    user_values = []
    
    while True:
        user_input = input("Enter a number (or press enter to stop): ")
        
        if user_input == '':
            break  # Exit loop on blank input
        try:
            # Convert input to float and append to list
            num = float(user_input)
            user_values.append(num)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    return user_values

# Main program
values = get_user_input()

if values:
    if isSorted(values):
        print("The list is sorted.")
    else:
        print("The list is not sorted.")
else:
    print("No values were entered.")



def bestOfTwo(list1, list2):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the lists using their indices
    for i in range(len(list1)):
        # Compare the values at the same index in both lists and append the greater one
        if list1[i] > list2[i]:
            result.append(list1[i])
        else:
            result.append(list2[i])
    
    return result

# Example usage:
list1 = [2, 4, -3, 1.2, 6, -10]
list2 = [3, 3, 2, 0, 100, -20]

# Call the function and display the result
best_list = bestOfTwo(list1, list2)
print("Best of two lists:", best_list)









def countRange(lst, start, end):
    count = 0
    # Iterate through the list and check if each value is within the given range
    for num in lst:
        if start <= num <= end:
            count += 1
    return count

# Main program to create a list and use the function
numbers = [1, 5, 8, 10, 15, 20, 25, 30, 35]

# Example usage: Count elements between 10 and 25 (inclusive)
start_range = 10
end_range = 25
result = countRange(numbers, start_range, end_range)

print(f"Count of elements between {start_range} and {end_range}: {result}")






def dispList(items):
    if len(items) == 0:
        return ""  # Return an empty string if the list is empty
    elif len(items) == 1:
        return items[0]  # Return the single item as a string
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"  # Join two items with "and"
    else:
        result = ""
        # Iterate through the items except the last one
        for i in range(len(items) - 1):
            result += items[i]  # Add the current item
            if i < len(items) - 2:
                result += ", "  # Add a comma after each item except the last one
        result += " and " + items[-1]  # Add "and" before the last item
        return result

# Example usage:
fruits1 = ['Apple', 'Banana', 'Orange', 'Pear', 'Mango']
print(dispList(fruits1))  # Output: Apple, Banana, Orange, Pear and Mango

fruits2 = ['Apple', 'Banana']
print(dispList(fruits2))  # Output: Apple and Banana





import random

# Initialize player scores
player1_score = 0
player2_score = 0

def scoreUpdate():
    global player1_score, player2_score, die1, die2
    
    # Check if die1 is greater than die2
    if die1 > die2:
        player1_score += (die1 - die2)  # Add the difference to player1's score
    elif die2 > die1:
        player2_score += (die2 - die1)  # Add the difference to player2's score

    # Check if scores are equal
    if player1_score == player2_score:
        player1_score = 0  # Reset player1's score
        player2_score = 0  # Reset player2's score

# Main game loop
while True:
    # Roll the dice
    die1 = random.randint(1, 6)  # Simulate rolling die 1
    die2 = random.randint(1, 6)  # Simulate rolling die 2
    
    print(f"Die1: {die1}, Die2: {die2}")
    
    # Update scores
    scoreUpdate()
    
    # Display current scores
    print(f"Player 1 Score: {player1_score}, Player 2 Score: {player2_score}")

    # Check for a winner
    if player1_score >= 20:
        print("Player 1 wins!")
        break
    elif player2_score >= 20:
        print("Player 2 wins!")
        break

