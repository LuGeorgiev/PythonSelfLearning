from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self ,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise Exception('Invalid input')
        self.__age = value

    @abstractmethod
    def produce_sound(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}'


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return 'Bau bau'


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return 'Kva kva'


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return 'Miau miau'


class Tomcat(Cat):
    def __init__(self, name, age, gender='Male'):
        Cat.__init__(self, name, age, gender='Male')

    def produce_sound(self):
        return 'MIAU MIAU'


class Kitten(Cat):
    def __init__(self, name, age, gender='Female'):
        Cat.__init__(self, name, age, gender='Female')

    def produce_sound(self):
        return 'miauuuuu'


animals_list = []
while True:
    kind = input()
    if kind == 'Beast!':
        break

    name, age, gender = input().split()
    obh_str = f'{kind}("{name}",{int(age)},"{gender}")'
    try:
        obj = eval(obh_str)
        animals_list.append(obj)
    except Exception as ex:
        print('Invalid input')

for animal in animals_list:
    print(animal)

