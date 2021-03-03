# Tuples are immutable, we can't reassign any value. Once the tuple is written, we can't change a value in it
t = (1, 2, 3)
print(t)

t = ('a', 'b', 'c', 'a')
# checking how many times a is in our tuple
print(t.count('a'))
# index will give us the first time our value appears in the tuple
print(t.index('a'))


