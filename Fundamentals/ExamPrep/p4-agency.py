from abc import ABC, abstractmethod


class Apartment (ABC):
    def __init__(self, id, rooms, baths, square_meters, price):
        self.id = id
        self.rooms = int(rooms)
        self.bath = int(baths),
        self.square_meters = int(square_meters)
        self.price = float(price)
        self.is_take = False

    @abstractmethod
    def __str__(self):
        return (f'{self.rooms} rooms place with {self.bath} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv.')


class LivingApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        Apartment.__init__(self, id, rooms, baths, square_meters, price)

    def __str__(self):
        return Apartment.__str__(self)


class OfficeApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        Apartment.__init__(self, id, rooms, baths, square_meters, price)

    def __str__(self):
        return Apartment.__str__(self)


data = input()
apartments_list = []
while not data == "start_selling":
    try:
        current_app = eval(data)
        apartments_list.append(current_app)
    except Exception as ex:
        print(ex)

    data = input()

data_list = input().split()
ids_list = list(map(lambda x: x.id, apartments_list))

while not (data_list[0] == "free" or data_list[0] == "taken"):
    command = data_list[0]
    id = data_list[1]
    if id in ids_list:
        current_apartment: Apartment = list(filter(lambda x: x.id == id, apartments_list))[0]
        if current_apartment.is_take:
            print(f'Apartment with id - {id} is already taken')
        elif command == "rent" and isinstance(current_apartment, LivingApartment):
            print(f'Apartment with id - {id} is only for selling!')
        elif command == "buy" and isinstance(current_apartment, OfficeApartment):
            print(f'Apartment with id - {id} is only for renting!')
        else:
            current_apartment.is_take = True
    else:
        print(f'Apartment with id - {id} does not exist!')
    data_list = input().split()

if data_list[0] == "taken":
    taken_apartments_list = list(filter(lambda a: a.is_taken == True, apartments_list))
    for apart in sorted(taken_apartments_list, key=lambda a: (a.price, -a.square_meters)):
        print(apart)
elif data_list[0] == "free":
    taken_apartments_list = list(filter(lambda a: a.is_taken == False, apartments_list))
    for apart in sorted(taken_apartments_list, key=lambda a: (-a.price, a.square_meters)):
        print(apart)
if len(taken_apartments_list) == 0:
    print('No information for this query')




# OfficeApartment("id_nim", 4, 2, 123, 2300)
# LivingApartment("00L", 2, 2, 173, 223000)
# OfficeApartment("i00A", 3, 2, 153, 23050)