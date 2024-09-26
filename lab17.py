a = [7,3,6,10,6,7,-2,7,5,-8,2,23]
print(a.index(max(a)))

b=sorted(a)
lessThanSeven=b.index(7)
print(b)
count=b.count(7)
secondLargest=b[len(b)-2]
print(f'numbers less than 7 are {lessThanSeven} and greater than seven are {len(b)-(lessThanSeven+count)} second largest number {secondLargest} is at index {a.index(secondLargest)}')


