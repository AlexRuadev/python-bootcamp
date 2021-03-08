class Animal():
    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


my_animal = Animal();
my_animal.who_am_i()
my_animal.eat()


class Dog(Animal):

    def __init__(self):
        #  Creating an instance of our Animal class in our Dog class so we can use Animal's method
        Animal.__init__(self)
        print('Dog Created')

    def who_am_i(self):
        print("I'm a dog")

    def bark(self):
        print('WOOF i am barking')


my_dog = Dog()
# Using Animal's method eat()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()


### Polymorphism ###
class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat(Animal):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


niko = Dog('niko')
felix = Cat('felix')


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

