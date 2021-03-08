mylist = [1, 2, 3]

myset = set()


# creating Dog class
class Dog():
    #  Clqss object attributes
    #  Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        #  creating attributes
        #  takes in an argument
        #  assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # expecting a boolean
        self.spots = spots

    # Methods
    def bark(self, number):
        print('Woof! My name is {} and I bark {} times'.format(self.name, number))


# creating an instance of our Dog class
my_Dog = Dog('German Sheperd', 'Felix', True)
print(my_Dog.species)
print(my_Dog.breed, my_Dog.name, my_Dog.spots)
#  using bark method
my_Dog.bark(5)


class Circle():
    # Class object attribute
    pi = 3.14

    # We can define a default parameter of 1 for our radius
    def __init__(self, radius=30):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle()
my_circle_circumference = my_circle.get_circumference()
my_circle_pi = my_circle.pi
my_circle_radius = my_circle.radius
my_circle_area = my_circle.area

print(my_circle_circumference)
print(my_circle_pi)
print(my_circle_radius)
print(my_circle_area)
