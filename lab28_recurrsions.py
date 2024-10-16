def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(100)) 




def permutations(elements):
    if len(elements) == 1:
        return [elements]

    perms = []
    for i in range(len(elements)):
        current = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        for perm in permutations(remaining_elements):
            perms.append([current] + perm)
    
    return perms

elements = [1,2,3]

for perms in permutations(elements):
    print(perms)







