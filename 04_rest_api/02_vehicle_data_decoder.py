"""
2.1.1.2 Vehicle data decoder/encoder
https://edube.org/learn/pcpp1-working-with-restful-apis/vehicle-data-decoder-encoder
Take a look at these two screenshots. They present two different use cases of the same program:
Command prompt -- python 01.py
Command prompt -- python 02.py
Your task is to write a code which has exactly the same conversation with the user and:
    defines a class named Vehicle, whose objects can carry the vehicle data shown above (the structure of the class
    should be deducted from the above dialog — call it "reverse engineering" if you want)
    defines a class able to encode the Vehicle object into an equivalent JSON string;
    defines a class able to decode the JSON string into the newly created Vehicle object.
Of course, some basic data validity checks should be done, too. We're sure you're careful enough to protect your code
from reckless users.
"""
import json


class Vehicle:
    def __init__(self, registration, year, passenger, mass):
        self.registration = registration
        self.year = year
        self.passenger = passenger
        self.mass = mass


class VehicleEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Vehicle):
            return w.__dict__
        else:
            return super().default(self, z)


class VehicleDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    @staticmethod
    def decode_vehicle(d):
        return Vehicle(**d)


def main():
    print('What can I do for you?\n',
          '1 - produce a JSON string describing a vehicle\n',
          '2 - decode a JSON string into vehicle data')
    choice = 0
    while choice not in ['1', '2']:
        choice = input('Your choice [1/2]: ')
    if choice == '1':
        registration = input('Registration number: ')
        while True:
            try:
                year = int(input('Year of production: '))
                break
            except ValueError:
                print("Year of production must be an integer value.")
                continue
        passenger = 0
        while passenger not in ['n', 'y']:
            passenger = input('Passenger [y/n]: ')
        if passenger == 'y':
            passenger = True
        else:
            passenger = False
        while True:
            try:
                mass = float(input('Vehicle mass: '))
                break
            except ValueError:
                print("Vehicle mass must be a number. (separator: .)")
                continue
        vehicle = Vehicle(registration, year, passenger, mass)
        print('Resulting JSON string is:\n',
              json.dumps(vehicle, cls=VehicleEncoder),
              '\nDone')
    else:
        vehicle_json = input('Enter vehicle JSON string: ')
        vehicle = json.loads(vehicle_json, cls=VehicleDecoder)
        print(vehicle.__dict__)


if __name__ == '__main__':
    main()
