import math

### to get all infos
# help(math)
###

value = 4.35

# Nearest low value
x = math.floor(value)
print(x)

# Nearest high value
x = math.ceil(value)
print(x)

# closest value
x = round(value)
print(x)


from math import pi
print(pi)



import random
# get a random integer between 0 & 100
x = random.randint(0,100)
print(x)


mylist = list(range(0,20))
print(mylist)

# grab a random item from the list
x = random.choice(mylist)
print(x)

# grab random items from the list with replacement (can pick few times the same item). k is the number of item we wanna pick
x = random.choices(population=mylist,k=10)
print(x)


# grab random items from the list without replacement (can't pick same item twice). k is the number of item we wanna pick
x = random.sample(population=mylist,k=5)
print(x)

random.shuffle(mylist)
print(mylist)