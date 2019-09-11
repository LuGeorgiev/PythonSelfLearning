class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print('Age have to be positive')
        else:
            self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value)<3:
            print("name should be more than 3 symbols")
        else:
            self.__name = value

    def __str__(self):
        return f'{self.name} {self.age}'

class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 15:
            print("Child's age must be less than 15")
        else:
            Person.__class__.fset(self, value)
            self.__age = value


person = Child("lu", -3)
