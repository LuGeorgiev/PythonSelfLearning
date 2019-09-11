class Animal:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name


class Dog(Animal):
    def __init__(self, name, age, number_of_legs: int):
        Animal.__init__(self, name, age)
        self.number_of_legs = number_of_legs

    def make_sound(self):
        return 'Bau Bauuuu'

    def __str__(self):
        return f'Dog: {self.name}, age: {self.age}, number of legs: {self.number_of_legs}'


class Cat(Animal):
    def __init__(self, name, age, iq: int):
        Animal.__init__(self, name, age)
        self.iq = iq

    def make_sound(self):
        return 'I am very intelligent cat... blah blah'

    def __str__(self):
        return f'Cat: {self.name}, age: {self.age}, IQ: {self.iq}'


class Snake(Animal):
    def __init__(self, name, age, cruelty_coef: int):
        Animal.__init__(self, name, age)
        self.crulety = cruelty_coef

    def make_sound(self):
        return 'PSsss I am snake'

    def __str__(self):
        return f'Snake: {self.name}, age: {self.age}, cruelty: {self.crulety}'


data_list = input().split()
animal_list = []
while not data_list[0].startswith("I'm"):
    if data_list[0] == 'talk':
        name = data_list[1]
        current_animal = list(filter(lambda x: x.name == name, animal_list))[0]
        print(current_animal.make_sound())
    else:
        kind = data_list[0]
        name = data_list[1]
        age = int(data_list[2])
        ability = int(data_list[3])
        if kind == 'Dog':
            dog = Dog(name, age, ability)
            animal_list.append(dog)
        elif kind == "Cat":
            cat = Cat(name, age, ability)
            animal_list.append(cat)
        elif kind == 'Snake':
            snake = Snake(name, age, ability)
            animal_list.append(snake)

    data_list = input().split()

dogs_list = filter(lambda x: isinstance(x, Dog), animal_list)
cats_list = filter(lambda x: isinstance(x, Cat), animal_list)
snakes_list = filter(lambda x: isinstance(x, Snake), animal_list)

sorted_animals = dogs_list + cats_list + snakes_list
for animal in sorted_animals:
    print(animal)

