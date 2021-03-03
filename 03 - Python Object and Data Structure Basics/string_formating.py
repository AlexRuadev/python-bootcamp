# Insert something in a string
print('This is a {} string '.format('INSERTED'))

# Inserting words with chosen index
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {2} {2} {2}'.format('fox', 'brown', 'quick'))

# We can use variable instead of using index, which is a better solution
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))

# Float formqting
result = 100 / 777
# Formating a floating {value:width.precision f}
print('The result was {r:1.3f}'.format(r=result))

### f strings , formatted strings litteral. New in PYTHON 3.6 ###
name = 'Jose'
age = 16
print(f'Hello, my name is {name} and i am {age}')
