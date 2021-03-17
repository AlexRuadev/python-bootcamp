from collections import Counter

mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3,]

# get the number of each number
print(Counter(mylist))

mylist = [1,1,'a',1,2,2,2,2,3,'a',3,3,3,'a',3,]
print(Counter(mylist))

myletters = 'Here we will count how many times each letter appears'
print(Counter(myletters))

mywords = 'Here we will count how many times each Word appears'
mywords = mywords.split()
print(Counter(mywords))


letters = 'aaaabbbbcccccccdddddddddd'
c = Counter(letters)
print(c)

# Most common will return a tuple with the most common letter in our Counter(letters)
c.most_common()
# Print the 2 most commons
print(c.most_common(2))


from collections import defaultdict

#  creating a default dictionnary, with default values being 0
d = defaultdict(lambda: 0)
d['correct'] = 100

print(d['correct'])

# Printing a key which isn't in our dictionnary will return the default value
print(d['test'])
