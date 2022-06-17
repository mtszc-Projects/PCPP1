"""
3.1.1.12 Advanced exceptions – the LAB
https://edube.org/learn/python-advanced-1/advanced-exceptions-the-lab
Try to extend the checklist script to handle more different checks, all reported as RocketNotReady exceptions.
Add your own checks for: batteries and circuits.
"""


class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


def batteries_check():
    try:
        batteries_capacity = 0.93
        assert batteries_capacity >= 0.95
        print(f'Batteries capacity:{batteries_capacity}%')
    except AssertionError as e:
        raise RocketNotReadyError('Batteries capacity too low.') from e


def circuits_check():
    try:
        print("\tCircuit 'a' voltage: ", circuits['a'])
        print("\tCircuit 'b' voltage: ", circuits['b'])
        print("\tCircuit 'c' voltage: ", circuits['c'])
        print("\tCircuit 'd' voltage: ", circuits['d'])
    except KeyError as e:
        raise RocketNotReadyError("There is not enough information from circuits reading.") from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
circuits = {'a': '1,5V', 'b': '3V', 'c': '9V'}
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
