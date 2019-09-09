class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


persone_1 = Person('Ivan', 'mail', 67)
persone_2 = Person('Marin', 'other', 37)
persone_3 = Person('Mira', 'female', 6)

print(persone_1.name)
print(persone_3.name)