

# def permutations(elements):
#     if (len(elements) == 1 or len(elements) == 0)  :
#         return [elements]
   

#     perms = []
#     for i in range(len(elements)):
#         current = elements[i]
#         remaining_elements = elements[:i] + elements[i+1:]
#         for perm in permutations(remaining_elements):
#             perms.append([current] + perm)
    
#     return perms

# elements = [1,2,3,6]







def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
terms=1000
for i in range(terms):
    print(factorial(terms))







memo = {}
def factorial(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)
    # memo[n] = result
    # print(memo)
    return memo


# def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result




### Task one ######

# for perms in permutations(elements):
#     print(perms)

### Task two ######
x=8
for i in range(1,x):
    print(factorial(i))

