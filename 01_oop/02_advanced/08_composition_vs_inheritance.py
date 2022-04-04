"""
2.8.1.7 LAB
https://edube.org/learn/python-advanced-1/lab-3
"""


class Tires:
    def __init__(self, size, pressure=2.0):
        self.size = size
        self.pressure = pressure

    def get_pressure(self):
        return self.pressure        

    def pump(self):
        self.pressure += 0.1


class Engine:
    def __init__(self, fuel_type):
        self.flag = 0
        self.fuel_type = fuel_type

    def start(self):
        self.flag = 1
        return "Starting the engine."
    
    def stop(self):
        self.flag = 0
        return "Engine is turning off."

    def get_state(self):
        return "Engine is off" if self.flag == 0 else "Engine is on."


class Vehicle:
    def __init__(self, vin, engine, tires):
        self.vin = vin
        self.engine = engine
        self.tires = tires


if __name__ == '__main__':
    city_tires = Tires(16)
    off_road_tires = Tires(18)
    electric_engine = Engine('electric')
    petrol_engine = Engine('petrol')
    car_1 = Vehicle(123456789, electric_engine, city_tires)
    car_2 = Vehicle(987654321, petrol_engine, off_road_tires)
    print(car_1.tires.size)
    print(car_1.tires.get_pressure())
    car_1.tires.pump()
    print(car_1.tires.get_pressure())
    print(car_1.engine.fuel_type)
    print(car_1.engine.get_state())
    print(car_1.engine.start())
    print(car_1.engine.get_state())
    print(car_1.engine.stop())
    print(car_1.engine.get_state())
    print(car_2.tires.size)
    print(car_2.tires.get_pressure())
    car_2.tires.pump()
    print(car_2.tires.get_pressure())
    print(car_2.engine.fuel_type)
    print(car_2.engine.get_state())
    print(car_2.engine.start())
    print(car_2.engine.get_state())
    print(car_2.engine.stop())
    print(car_2.engine.get_state())
