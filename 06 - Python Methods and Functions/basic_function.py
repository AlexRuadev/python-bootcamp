def say_hello():
    print('hello')


say_hello()


# Defqult is used in case we don't give a name when we call the fonction, it can be anything
def say_hello(name='Default'):
    print(f'hello {name}')


say_hello()


def add_num(num1, num2):
    return num1 + num2


summary = add_num(5, 7)
print(summary)
