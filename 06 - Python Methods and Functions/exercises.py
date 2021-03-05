# write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # Both numbers are even
        return min(a, b)
    else:
        # one or both numbers are odd
        return max(a, b)


winner = lesser_of_two_evens(2, 8)

print(winner)


# write a function takes a two word string qnd returns true if both words begin with the sqme letter
def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)

    return wordlist[0][0] == wordlist[1][0]


check = animal_crackers('Level Lama')
check2 = animal_crackers('Level Tama')
print(check)
print(check2)


# write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    first_half = name[:3]
    second_part = name[3:]

    return first_half.capitalize() + second_part.capitalize()


name = old_macdonald('macdonald')
print(name)
