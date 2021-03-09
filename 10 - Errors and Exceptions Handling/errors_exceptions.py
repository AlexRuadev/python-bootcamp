def add(n1, n2):
    print(n1 + n2)


# trying to add int and string, handling our error message with except
try:
    # want to attempt this code but it may have an error
    result = 10 + '10'
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

print(result)
