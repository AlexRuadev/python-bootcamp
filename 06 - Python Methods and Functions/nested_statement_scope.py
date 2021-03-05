x = 25


def printer(x):
    print(f'X is {x}')

    # Local reassignement on a global variable
    x = 'New Value'
    print(f'I JUST LOCALLY CHANGED GLOBAL X to {x}')
    return x


#  Reassigning value
x = printer(x)
print(x)


#  Function in a function
def greet():
    name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()


greet()
