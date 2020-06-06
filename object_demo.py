class Dog:
    # class attribute = static variable
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

print(type(Dog('a', 1)))