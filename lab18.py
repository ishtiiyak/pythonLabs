##--------  Task One --------##

# def max(arr):
#     max_sum = float('-inf')
#     max_sublist = []

#     for sublist in arr:
#         current_sum = sum(sublist)
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_sublist = sublist

#     return max_sublist


# a = [[2, 3, 1], [5, 6, 1, 0, -2], [3, 4], [5, 6, 7, 2]]
# print(max(a))  


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


myList=[1,2,3,4,5,6,7,8,9]
split=5

def splitList(list,splitIndex):
    partOne=[]
    partTwo=[]
    for i in range(split):
        partOne.append(list[i])
    for j in range(split,len(list)):
        partTwo.append(list[j])
    return[partOne,partTwo]    
  

print(f'first part is {splitList(myList,split)[0]} and last past is{splitList(myList,split)[1]}')     




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

def mergeLists(listOne,listTwo):
    # newListA=[]
    # for i in range(len(listOne)):
    #     a=[]
    #     a.append(listOne[i])
    #     a.append(listTwo[i])
    #     newListA.append(a)
    # return newListA
    b = []
    c = []
    prev = 0
    for i in listOne:
        b += i
        b += listTwo[prev]
        prev += 1
    c.append(b)
    return c
print(mergeLists([[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]))