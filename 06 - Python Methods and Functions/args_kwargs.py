# *args = arguments
# **kwargs = key word arguments

# we can pass parameters = 0, so we don't need to declare them in our function, but in case we can use them

def myfunc(a, b, c=0, d=0, e=0):
    # Returns 5% of the sum of a and b
    return sum((a, b, c, d, e)) * 0.05

# args will return a list of tuples
def myfunc0(*args):
    print(args)

myfunc0(10,20,30,40)


# kwargs return a dictionnary
def myfunc(**kwargs):
    # we have a dictionnary with kwargs
    print(kwargs)

    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


myfunc(fruit='Apple', veggie='lettuce')

# passing args and kwargs
def myfunc1(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc1(10, 20, 30, fruit='orange', food='eggs', animal='dogs')
