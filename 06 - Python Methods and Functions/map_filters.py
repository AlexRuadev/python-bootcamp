# The map function is used to execute the function on each item of our list
# which means 1**2 2**2 3**2 etc etc


def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums):
    print(item)

x = list(map(square, my_nums))
print(x)


# Return Even if the name has even sum of letter, otherwise return first letter
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Allany', 'Tristan']
y = list(map(splicer, names))
print(y)


#  Filter will filter based off our function
def check_even(num):
    return num % 2 == 0


my_num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
z = list(filter(check_even, my_num1))
print(z)



def square(num):
    result = num ** 2
    return result

a = square(2)
print(a)