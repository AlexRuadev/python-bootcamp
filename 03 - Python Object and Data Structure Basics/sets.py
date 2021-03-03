# Sets are unordered collections of unique elements. we can't have twice the same element
myset = set()

# add an element to our set
myset.add(1)
myset.add(2)

print(myset)

# creating a list with duplicates values
mylist = [1, 1, 1, 4, 4, 65, 8, 5, 3, 554, 84, 4, 2, 5, 24, 4, 58, 224, 2]

# using set to clear duplicatas in the list
mylist = set(mylist)

# we get a set back
print(mylist)
print(type(mylist))

# passing our set to a list again
mylist = list(mylist)
print(mylist)
print(type(mylist))
