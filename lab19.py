#--------  Task One --------##

def max(arr):
    max_sum = float()
    max_sublist = []

    for sublist in arr:
        current_sum = sum(sublist)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sublist = sublist

    return max_sublist


a = [[2, 3, 1], [5, 6, 1, 0, -2], [3, 4], [5, 6, 7, 2]]
print(max(a))  


##--------  Task Two --------##




# def split_list(my_list, length):
#     mid = len(my_list) // 2
#     first_part = my_list[length]
#     second_part = my_list[length]
#     return first_part, second_part

# Example usage:
# original_list = [1, 2, 3, 4, 5, 6, 7, 8]
# length = 3
# first_part, second_part = split_list(original_list, length)

# print("Original list:", original_list)
# print(f"First part ({length} elements):", first_part)
# print("Second part:", second_part)




# A = [[-2,1,4],[5,7,0],[1,2,4]]
# for i in A:
#     for j in i:
#         print(f'{j:6.2f}',end=' ')
#     print()

# A=[]
# for r in range(3):
#     print(f'Enter row-{r+1}.')
#     a=[]
#     for c in range(3):
#         n=eval(input(f'Enter element-{c+1}:'))
#         a.append(n)
#     A.append(a)
# print(A)


# Write a program to split a given list into two parts where the length of the first part of the list is 
# givena =[1,2,3,4,5,6,7,8]


# myList=[1,2,3,4,5,6,7,8,9]
# split=5

# def splitList(list,splitIndex):
#     partOne=[]
#     partTwo=[]
#     for i in range(split):
#         partOne.append(list[i])
#     for j in range(split,len(list)):
#         partTwo.append(list[j])
#     return[partOne,partTwo]    
  

# print(f'first part is {splitList(myList,split)[0]} and last past is{splitList(myList,split)[1]}')     




# Write a Python program to Merge two given lists of sublists in a way that each sublist on 
# corresponding index merges together. Again, do it by creating a function named as 
# mergeSubLists having two input arguments (assuming both are lists of equal number of 
# sublists) and output as a bigger list. See the example of input and output here:
# 5 | P a g e
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Merged list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]

# def mergeLists(listOne,listTwo):
#     # newListA=[]
#     # for i in range(len(listOne)):
#     #     a=[]
#     #     a.append(listOne[i])
#     #     a.append(listTwo[i])
#     #     newListA.append(a)
#     # return newListA
#     b = []
#     c = []
#     prev = 0
#     for i in listOne:
#         b += i
#         b += listTwo[prev]
#         prev += 1
#     c.append(b)
#     return c
# print(mergeLists([[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]))




# Task 1: Function to find the sublist with the maximum sum
def maxSum(list_of_sublists):
    max_sum = float('-inf')  # Initialize max sum to negative infinity
    max_sublist = []

    for sublist in list_of_sublists:
        current_sum = sum(sublist)  # Sum the current sublist
        if current_sum > max_sum:
            max_sum = current_sum
            max_sublist = sublist

    return max_sublist

# Task 2: Split a list into two parts at a given length
def splitListAt(lst, length):
    return lst[:length], lst[length:]  # Split using list slicing

# Task 3: Split list into sublists of size n
def splitList(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i+n])  # Append slices of size n
    return result

# Task 4: Merge two lists of sublists by corresponding indices
def mergeSubLists(list1, list2):
    merged_list = []
    for i in range(len(list1)):
        merged_list.append(list1[i] + list2[i])  # Merge sublists at the same index
    return merged_list

# Main Program to demonstrate all tasks
if __name__ == "__main__":
    # Task 1 Example: Find sublist with the highest sum
    a = [[2, 3, 1], [5, 6, 1, 0, -2], [3, 4], [5, 6, 7, 2]]
    print("Sublist with maximum sum:", maxSum(a))  # Output: [5, 6, 7, 2]

    # Task 2 Example: Split list into two parts
    lst = [1, 2, 3, 4, 5, 6, 7]
    first_part, second_part = splitListAt(lst, 4)
    print("First part:", first_part)  # Output: [1, 2, 3, 4]
    print("Second part:", second_part)  # Output: [5, 6, 7]

    # Task 3 Example: Split list into sublists of size n
    a = [2, 3, 4, 2, 5, 1, 6, 7, 8, 10, 22, 3, 13]
    print("List split into sublists of size 4:", splitList(a, 4))
    # Output: [[2, 3, 4, 2], [5, 1, 6, 7], [8, 10, 22, 3], [13]]

    # Task 4 Example: Merge two lists of sublists by index
    list1 = [[1, 3], [5, 7], [9, 11]]
    list2 = [[2, 4], [6, 8], [10, 12, 14]]
    print("Merged sublists:", mergeSubLists(list1, list2))
    # Output: [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]






import random
import time

# Task 1: Marks Calculation (Subject/Student Analysis)
class_marks = [
    [89, 91, 68, 88, 93],
    [78, 79, 87, 78, 67],
    [94, 83, 69, 79, 82],
    [67, 78, 77, 82, 66],
    [88, 82, 87, 77, 69],
    [93, 55, 90, 82, 67],
    [76, 69, 86, 75, 94],
    [66, 77, 67, 64, 83],
    [82, 79, 83, 71, 68],
    [59, 83, 88, 84, 79]
]

subjects = ["Calculus", "Algebra", "Programming", "Electronics", "Statistics"]

def analyze_subject(sub):
    column = [row[sub] for row in class_marks]
    avg = sum(column) / len(column)
    max_marks = max(column)
    min_marks = min(column)
    max_roll = column.index(max_marks) + 1
    min_roll = column.index(min_marks) + 1
    print(f"In {subjects[sub]} average score is:






          
def column(A,c): 
    a=[] 
    for i in range(len(A)): 
        a.append(A[i][c]) 
    return a 
 
## Main Program ## 
A = [[-2,1,4],[5,7,0],[1,2,4]] 
col=column(A,2) 
print(col) 
print(sum(col))
          



def det2(A):
    'Returns the determinant of 2x2 Matrix A'
    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

def det3(A):
    'Returns the determinant of 3x3 Matrix A'
    return (A[0][0] * det2([A[1][1:], A[2][1:]])) - (A[0][1] * det2([A[1][[0, 2]], A[2][[0, 2]]])) + (A[0][2] * det2([A[1][:2], A[2][:2]]))

### Main Program Starts here ###
C = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
print(f"Determinant of C is: {det3(C)}")





def det2(A):
    'Returns the determinant of 2x2 Matrix A'
    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

def inv2(A):
    'Returns the inverse of A'
    determinant = det2(A)
    if determinant == 0:
        return "Matrix has no inverse"
    return [[A[1][1] / determinant, -A[0][1] / determinant],
            [-A[1][0] / determinant, A[0][0] / determinant]]

def dispMat(A):
    'Displays matrix A of any size'
    for row in A:
        print(" | ".join(f"{x:.2f}" for x in row))

### Main Program Starts here ###
B = [[2, 4], [3, 1]]
print("Inverse of B is: ")
dispMat(inv2(B))









grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def displayGrid():
    for row in grid:
        print(f'{row[0]} | {row[1]} | {row[2]}')
        if grid.index(row) < 2:
            print("----------")

def fillSlot(s, mark):
    global grid
    c = (s % 3) - 1
    r = abs(s - 1) // 3
    if grid[r][c] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False
    grid[r][c] = mark
    return True

def isWinner():
    # Check rows, columns, and diagonals
    for row in grid:
        if row[0] == row[1] == row[2]:
            return True
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col]:
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
        return True
    return False

### Main Program Starts here ###
turns = 0
while turns < 9:
    displayGrid()
    if turns % 2 == 0:
        print("Player 1 Turn (X)")
        p = int(input("Enter the slot number: "))
        if fillSlot(p, 'X'):
            if isWinner():
                displayGrid()
                print("Player 1 wins!")
                break
    else:
        print("Player 2 Turn (O)")
        p = int(input("Enter the slot number: "))
        if fillSlot(p, 'O'):
            if isWinner():
                displayGrid()
                print("Player 2 wins!")
                break
    turns += 1
else:
    print("Game ended in a draw.")
