mylist = [1, 2, 3]

# range generates the number all the way to the number indicated but not including it
for num in range(10):
    print(num)

# range from 3 to 10, excluding 10
for num in range(3, 10):
    print(num)

# range from 0 to 10, excluding 10, going 2 by 2
for num in range(0, 10, 2):
    print(num)

# for every characters in our word string, printing the index value location for each letter
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

# enumerate returns back index counter and the object itself
word1 = 'akjdgierg'
for index, letter in enumerate(word1):
    print(index)
    print(letter)
    print('\n')

# Zip function will return back a tuples. zip function is putting together lists
# zip function will only matches the shortes list even if there are more items in another one
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
mylist3 = [100, 200, 300, 400, 500, 600, 700]

for item in zip(mylist1, mylist2, mylist3):
    print(item)
# get back only a certaine list
for a, b, c in zip(mylist1, mylist2, mylist3):
    print(c)
