my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we can choose the variable name
for numbers in my_list:
    print(numbers)

# Printing toto as much times as we have item in the list
for num in my_list:
    print('toto')

for num in my_list:
    # printing even numbers
    if num % 2 == 0:
        print(num)
    # printing odd numbers
    else:
        print(f'Odd number: {num}')

list_sum = 0
# for every numbers in he list, i take old value from sum and add new number, and reassign it
for num in my_list:
    list_sum = list_sum + num
print(list_sum)

mystring = 'Hello World'

for letter in mystring:
    print(letter)

### Tuples ###
tup = (1, 2, 3)
for item in tup:
    print(item)

my_tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in my_tuple_list:
    print(item)

# printing tuples values one by one instead of 2 by 2 as in list
for a, b in my_tuple_list:
    print(a)
    print(b)

# iterations over a dictionnary
d = {'k1':1, 'k2':2, 'k3':3}
# by default, in dictionnaries it loops only over the key
for item in d:
    print(item)

# to loop over keys and values we need to do
for item in d.items():
    # we are getting back tuples
    print(item)

# or
for key, value in d.items():
    # we are getting back keys and values
    print(key, value)