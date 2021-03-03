# list are mutable
# Creating a list
my_list = [1, 2, 3]
# print the index 2 of the list
print(my_list[2:])

# print the last two elements of the list
my_list1 = ['STRING', 100, 23.2]
print(my_list1[1:])

my_list2 = ['one', 'two', 'three']

# list concatenation
print(my_list + my_list1)

# Storing our concatenated list in a variable
new_list = my_list + my_list1
print(new_list)

# Changing elements in a list at index 0
new_list[0] = 'ONE ALL CAPS'
print(new_list)

# adding an element to the last position of the list
new_list.append('last added')
print(new_list)

# removing the last item from a list
new_list.pop()
print(new_list)

# remove a chosen index item (0)
new_list.pop(0)
print(new_list)

# sorting lists
letter_list = ['a', 'e', 'x', 'b', 'h']
letter_list.sort()
print(letter_list)

num_list = [44, 9, 7, 56, 8]
num_list.sort()
print(num_list)

# reverse lists
num_list.reverse()
print(num_list)

