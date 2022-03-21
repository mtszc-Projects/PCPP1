"""
1.1.1.6 Classes, Instances, Attributes, Methods — the LAB
https://edube.org/learn/python-advanced-1/classes-instances-attributes-methods-the-lab
"""


class Mobile:
    def __init__(self, number):
        self.number = number

    def turn_on(self) -> str:
        return f'mobile phone {self.number} is turned on'

    @staticmethod
    def turn_off() -> str:
        return f'mobile phone is turned off'

    @staticmethod
    def call(number: str) -> str:
        return f'calling {number}'


mobile_1 = Mobile('01632-960004')
mobile_2 = Mobile('01632-960012')

print(mobile_1.turn_on())
print(mobile_2.turn_on())
print(mobile_1.call('555-34343'))
print(mobile_1.turn_off())
print(mobile_2.turn_off())
