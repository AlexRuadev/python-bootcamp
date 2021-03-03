# Print only the words that start with s in this sentence
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

# print all even numbers from 0 to 10
even = list(range(0, 11, 2))
print(even)

# use list co;prehension to create a list of number from 1-50 divisible by 3
list = [x for x in range(1, 51) if x % 3 == 0]
print(list)

# write progrra; the prints integer from 1 to 100, but for mmultiples of 3 print "Fizz", multiples of 5 "Buzz"m for
# numbers which are multiple of both 3 and 5 print "FizzBuzz"
for num in range(1,100):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)