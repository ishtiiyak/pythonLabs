def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(100)) 




def permutations(elements):
    if len(elements) == 1:
        return [elements]

    perms = []
    for i in range(len(elements)):
        # Take one element
        current = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        # Generate all permutations of the remaining elements
        for perm in permutations(remaining_elements):
            perms.append([current] + perm)

    return perms

# Example usage:
elements = [1, 2, 3,9]
# print(permutations(elements))




