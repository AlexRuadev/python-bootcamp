# Top open a text file and store it in my_file variable
with open('../text.txt') as my_file:
    content = my_file.read()
    print(content)

# Open and Read our file
with open('../text.txt', mode='r') as my_file:
    content = my_file.read()
    print(content)

with open('../text.txt', mode='a') as f:
    y = f.write("\ni'm adding another line")
    print(y)

with open('../text2.txt', mode='w') as y:
    y.write('I created this file')

# mode = 'r' read only
# mode = 'w' write only (will overwrite file or create new)
# mode = 'a' append only (adding to the file)
# mode = 'r+' reading and writing
# mode = 'w+' writing and reading (overwrites existing files or creates new file)



