text = "The agent's phone number is 408-555-1234. Call soon"

# checking if the string 'phone' is in our text variable
x = 'phone' in text
print(x)

import re

pattern = 'phone'
match = re.search(pattern, text)
# the span in the match result will give us the index characters number of our word phone
print(match)

text = 'My phone once, my phone twice'
matches = re.findall('phone', text)
# will return how many matches for our word will be in our variable
print(matches)

# Get all spans when we have multiples matches
for match in re.finditer('phone', text):
    print(match.span())
    print(match.group())


# get our phone form
text = "The agent's phone number is 408-555-1234. Call soon"

# we use the r for pattern for regular expressions. in case we're looking for a phone number and we know it forms,
# we can always find it with a regular expression
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)

# printing the phone number itself
print(phone.group())


# using quantifiers to simulate a repetition of the same character
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)

# taking multiple pattern code, each pattern codes are separated as a group with parenthesis and it compiles them in
# a single regular expression
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
# Returning each group indiviually
print(results.group(1))
print(results.group(2))
print(results.group(3))
