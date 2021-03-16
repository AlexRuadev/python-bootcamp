# passing a function within another function or calling a function within another function

def hello(name='Jose'):
    print('The hello() function has been executed')

    # we can only execute greet() and welcome() function inside of hello() function
    def greet():
        return '\t This is the greet() function inside hello!'

    def welcome():
        return '\t This is welcome inside hello()'


    print("I am going to return a function!")

    if name == "Jose":
        return greet()
    else:
        return welcome()


my_new_func = hello('Jose')


def cool():

    def super_cool():
        return 'I am very cool'

    return super_cool()

some_func = cool()

#  The cool() function will return our super_cool() function
print(some_func)




# Pass in function into another function
def bye():
    return 'bye Jose'

def other(some_def_func):
    print('Other code runs here')
    print(some_def_func())

# will print our bye() function inside other() function
print(other(bye))




def new_decorator(original_function):

    def wrap_func():
        print('1 Some extra code, before the original function')

        original_function()

        print('2 Some extra code, after the original function')

    return wrap_func()


#  passing our func_needs_decorator() inside our original_function() which is inside new_decorator()
def func_needs_decorator():
    print('3 I want to be decorated!!')

decorated_func = new_decorator(func_needs_decorator)

print(decorated_func)



@new_decorator
def func_needs_decorator():
    print('3 I want to be decorated!!')

func_needs_decorator()
