class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates
    @property
    def speed(self):
        return self._speed
    @property
    def brand(self):
        return self._brand
    @property
    def year(self):
        return self._year
    @property
    def number(self):
        return self._number

    @coordinates.setter
    def coordinates(self, coordinates):
        if len(coordinates) == 2 and all(isinstance(coordinate, int) and 0 <= coordinate <= 1000 for coordinate in coordinates):
            self._coordinates = coordinates
        else:
            raise ValueError("Неверный формат")

    @speed.setter
    def speed(self, speed):
        if isinstance(speed, int) and 0 <= speed <= 1000:
            self._speed = speed
        else:
            raise ValueError("Неверный формат")


    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError("Неверный формат")

    @year.setter
    def year(self, year):
        if isinstance(year, int) and 0 <= year <= 2023:
            self._year = year
        else:
            raise ValueError("Неверный формат")

    @number.setter
    def number(self, number):
        if isinstance(number, str):
            self._number = number
        else:
            raise ValueError("Неверный формат")

    def __str__(self):
        return f"Координаты: X: {self._coordinates[0]}, Y: {self._coordinates[1]}, Скорость: {self._speed}, Марка: {self._brand}, Год: {self._year}, Номер: {self._number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self._coordinates[0] <= pos_x + length and pos_y >= self._coordinates[1] >= pos_y - width

class Passenger():

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int) and 0 < passengers_capacity <= 1000:
            self.__passengers_capacity = passengers_capacity
        else:
            raise ValueError("Неверный формат")

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and 0 <= number_of_passengers <= 1000:
            self.__number_of_passengers = number_of_passengers
        else:
            raise ValueError("Неверный формат")

class Cargo():
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int) and 0 <= carrying <= 1000:
            self.__carrying = carrying
        else:
            raise ValueError("Неверный формат")


class Plane(Transport):
    def __init__(self, height, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and 0 <= height <= 10000:
            self._height = height
        else:
            raise ValueError("Неверный формат")

class Auto(Transport): #вы сказали, что нужно добавить какое-то поле, я так понял, что любое на свое усмотрение
    def __init__(self, drivers_license_category, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self._drivers_license_category = drivers_license_category

    @property
    def drivers_license_category(self):
        return self._drivers_license_category

    @drivers_license_category.setter
    def drivers_license_category(self, drivers_license_category):
        valid_license_categories = ['A', 'B', 'C', 'D', 'BE', 'CE', 'DE', 'Tm', 'Tb', 'M', 'A1', 'B1', 'C1', 'D1', 'C1E', 'D1E']
        if drivers_license_category in valid_license_categories:
            self._drivers_license_category = drivers_license_category
        else:
            raise ValueError("Неверный формат")



class Ship(Transport):
    def __init__(self, port, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self._port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            self._port = port
        else:
            raise ValueError("Неверный формат")

class Car(Auto):
    def __init__(self, body_type, drivers_license_category, coordinates, speed, brand, year, number):
        super().__init__(drivers_license_category, coordinates, speed, brand, year, number)
        self._body_type = body_type

    @property
    def body_type(self):
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        if isinstance(body_type, str):
            self._body_type = body_type
        else:
            raise ValueError("Неверный формат")


class Bus(Auto, Passenger):
    def __init__(self, bus_type, drivers_license_category, coordinates, speed, brand, year, number):
        super().__init__(drivers_license_category, coordinates, speed, brand, year, number)
        self._bus_type = bus_type

    @property
    def bus_type(self):
        return self._bus_type

    @bus_type.setter
    def bus_type(self, bus_type):
        if isinstance(bus_type, str):
            self._bus_type = bus_type
        else:
            raise ValueError("Неверный формат")


class CargoAuto(Auto, Cargo):
    def __init__(self, cargo_capacity, drivers_license_category, coordinates, speed, brand, year, number):
        super().__init__(drivers_license_category, coordinates, speed, brand, year, number)
        self._cargo_capacity = cargo_capacity

    @property
    def cargo_capacity(self):
        return self._cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, cargo_capacity):
        if isinstance(cargo_capacity, int) and 0 < cargo_capacity < 1000:
            self._cargo_capacity = cargo_capacity
        else:
            raise ValueError("Неверный формат")


class Boat(Ship):
    def __init__(self, boat_type, port, coordinates, speed, brand, year, number):
        super().__init__(port, coordinates, speed, brand, year, number)
        self._boat_type = boat_type

    @property
    def boat_type(self):
        return self._boat_type

    @boat_type.setter
    def boat_type(self, boat_type):
        if isinstance(boat_type, str):
            self._boat_type = boat_type
        else:
            raise ValueError("Неверный формат")


class PassengerShip(Ship, Passenger):
    def __init__(self, ship_displacement, port, coordinates, speed, brand, year, number):
        super().__init__(port, coordinates, speed, brand, year, number)
        self._ship_displacement = ship_displacement

    @property
    def ship_displacement(self):
        return self._ship_displacement

    @ship_displacement.setter
    def ship_displacement(self, ship_displacement):
        if isinstance(ship_displacement, int) and 0 < ship_displacement < 1000:
            self._ship_displacement = ship_displacement
        else:
            raise ValueError("Неверный формат")


class CargoShip(Ship, Cargo):
    def __init__(self, cargo_capacity, port, coordinates, speed, brand, year, number):
        super().__init__(port, coordinates, speed, brand, year, number)
        self._cargo_capacity = cargo_capacity

    @property
    def cargo_capacity(self):
        return self._cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, cargo_capacity):
        if isinstance(cargo_capacity, int) and 0 < cargo_capacity < 1000:
            self._cargo_capacity = cargo_capacity
        else:
            raise ValueError("Неверный формат")

class Airplane(Plane, Passenger):
    def __init__(self, airplane_type, height, coordinates, speed, brand, year, number):
        super().__init__(height, coordinates, speed, brand, year, number)
        self._airplane_type = airplane_type

    @property
    def airplane_type(self):
        return self._airplane_type

    @airplane_type.setter
    def airplane_type(self, airplane_type):
        if isinstance(airplane_type, str):
            self._airplane_type = airplane_type
        else:
            raise ValueError("Неверный формат")


# class Seaplane(Plane, Ship): # не работает этот класс,у меня закончились идеи как это исправить
#     def __init__(self, seaplane_type, height, coordinates, speed, brand, year, number, port):
#         # super().__init__(height, coordinates, speed, brand, year, number)
#         # super().__init__(port, coordinates, speed, brand, year, number)
#         Plane.__init__(self, height, coordinates, speed, brand, year, number)
#         Ship.__init__(self, port, coordinates, speed, brand, year, number)
#         self._seaplane_type = seaplane_type
#
#     @property
#     def seaplane_type(self):
#         return self.seaplane_type
#
#     @seaplane_type.setter
#     def seaplane_type(self, seaplane_type):
#         if isinstance(seaplane_type, str):
#             self._seaplane_type = seaplane_type
#         else:
#             raise ValueError("Неверный формат")