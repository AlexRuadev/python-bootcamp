try:
    # introducing an error with "r" instead of "w"
    f = open('testfile', 'w')
    f.write('Write a test line')

except TypeError:
    # if we have a type error, print the following
    print('There was a type error')

except:
    print('There is another exception error')

#  Finally will always run the code, no matter what
finally:
    print('I always run')


def ask_for_int():
    # Creating a loop to repeat our function until an int is provided and there's no more errors
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            # break the loop if we have a "Yes thank you"
            break

        finally:
            print("End of try/except/finally")
            print("I'm always running at the end")


# run this and write a string for an error, or an integer for it to print our finally
ask_for_int()
