import os
from functools import reduce
import operator
import csv

class BaseCar:
    """Класс базовой машины"""

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self
        self.car_type = car_type

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    """Класс машин легкового класса"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    """Класс грузового автомобиля"""

    def __init__(self, car_type, brand, photo_file_name, body_whl, carrying):
        super().__init__(car_type, brand, photo_file_name, carrying)
        if body_whl == '': body_whl = '0x0x0'
        self.body_whl = body_whl
        self.body_width, self.body_height, self.body_length = [float(x) for x in body_whl.split('x')]

    def get_body_volume(self):
            #w, h, l = [float(x) for x in d.split('x')]
        if self.body_whl == '':
            return 0.0
        return reduce(operator.mul, [float(x) for x in self.body_whl.split('x')])


class SpecMachine(BaseCar):
    """Класс машин специального назначения"""

    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):

    car_list = []

    try:
        with open(csv_filename) as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                if len(row) != 7:
                    continue

                if row[0] == 'car':
                    print(row[0], row[1], row[2], row[3], row[5])
                    c = Car(row[0], row[1], row[2], row[3], row[5])
                elif row[0] == 'truck':
                    print(row[0], row[1], row[3], row[4], row[5])
                    c = Truck(row[0], row[1], row[3], row[4], row[5])
                    print(c.get_body_volume())
                elif row[0] == 'spec_machine':
                    print(row[0], row[1], row[3], row[5], row[6])
                    c = SpecMachine(row[0], row[1], row[3], row[5], row[6])

                car_list.append(c)

    except FileNotFoundError as e:
        print(e)

    return car_list


a = get_car_list('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv')

for c in a:
    print(c.__dict__)
