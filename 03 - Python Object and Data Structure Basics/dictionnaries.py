# create our first dictionary
my_dictionary = {'key1': 'value1', 'key2': 'value2'}
print(my_dictionary)

# printing our first value using key
print(my_dictionary['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.54, 'bananas': 0.99, 'milk': 5.45}
# getting the price or oranges
print(prices_lookup['oranges'])

# dictionaries can contain lists or other dictionaries
d = {'k1': 123, 'k2': [1, 4, 2, 23], 'k3': {'insideKey': 100}, 'k4': ['a', 'b', 'c']}
print(d['k2'])

# adding a key and value to our dictionary
d['k5'] = 300
print(d)
# getting 100 value
print(d['k3']['insideKey'])

# grabbing the c letter in our k4 list and making it uppercase
my_value = d['k4'][2].upper()
print(my_value)

# changing value in our dictionary
d['k1'] = 'new value'
print(d)

# grabbing all the keys
d = {'k1': 123, 'k2': [1, 4, 2, 23], 'k3': {'insideKey': 100}, 'k4': ['a', 'b', 'c']}
print(d.keys())

# grabbing all the values
print(d.values())

# grabbing all keys with values
print(d.items())

