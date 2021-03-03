# using  for loop

mystring = 'hello first'
mylist = []
for x in mystring:
    mylist.append(x)
print(mylist)

# using a flattened for loop
mystring = 'Hello'
mylist = [letter for letter in mystring]
print(mylist)

mylist = [num for num in range(0, 11)]
print(mylist)
