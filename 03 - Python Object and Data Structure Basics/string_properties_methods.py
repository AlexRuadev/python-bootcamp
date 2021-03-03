# Strings are not mutanble. We can't use indexing to change individual elements of a string. To replace them,
# we need to slice them to change a letter

name = 'Sam'
#  Replace Sam by Pam
last_letters = name[1:]

print(last_letters)

pam = 'P' + last_letters
print(pam)

# Add the forgotten d in this name
name1 = 'Alexanre'

first_letters = name1[:6]
last = name1[6:]
full_name = first_letters + 'd' + last

print(full_name)

x = 'Hello World my name is Tony'
# Split method will put each word in a list. It splits on the white space by default
print(x.split())
# Split at each o
print(x.split('o'))
