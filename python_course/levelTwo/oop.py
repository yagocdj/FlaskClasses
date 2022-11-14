# myList = [1, 2, 3]
# myList.append(4)
# print(type(myList))
# print(type(12))
# print(type(13.5))

# class Dog():

#     # CLASS OBJECT ATTRIBUTES
#     species = 'mammal'

#     def __init__(self, breed, name) -> None:
#         self.breed = breed
#         self.name = name

# sam = Dog('Huskie', 'Frankie')
# new_dog = Dog('Golden', 'Cindy')

# print(sam.breed)
# print(sam.name)
# print(sam.species)
# print(new_dog.species)


# class Circle():

#     PI = 3.14

#     def __init__(self, radius=1) -> None:
#         self.radius = radius

#     def area(self):
#         return self.radius ** 2 * self.PI

#     def circumfrence(self):
#         return 2 * self.PI * self.radius

# my_circle = Circle(10)
# print(my_circle.radius)
# print(my_circle.area())
# print(my_circle.circumfrence())

class Animal():

    def __init__(self, fur) -> None:
        self.fur = fur

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):
    
    def __init__(self, fur) -> None:
        Animal.__init__(self, fur)
        print("Dog created")

    def report(self):
        print('I am a dog!')

d = Dog('Fuzzy')
print(d.fur)
d.eat()
d.report()