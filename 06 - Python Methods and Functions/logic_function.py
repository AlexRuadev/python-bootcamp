def even_check(number):
    result = number % 2 == 0
    return result


even = even_check(20)
print(even)

even = even_check(21)
print(even)

########################################
# return true if any number is even inside a list
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False


# it prints True because 2 is an even number
even_list = check_even_list([1, 2, 3])
print(even_list)

# no even numbers, return false
even_list = check_even_list([1, 3])
print(even_list)

##################################
# return all even numbers in a list
def return_even_numbers(num_list):
    # placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


even_numbers_list = return_even_numbers([1,2,3,4,5,6,7,8,9,10])
print(even_numbers_list)