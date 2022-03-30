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


if __name__ == "__main__":
    mobile_1 = Mobile('01632-960004')
    mobile_2 = Mobile('01632-960012')
    assert mobile_1.turn_on() == 'mobile phone 01632-960004 is turned on'
    assert mobile_2.turn_on() == 'mobile phone 01632-960012 is turned on'
    assert mobile_1.call('555-34343') == 'calling 555-34343'
    assert mobile_1.turn_off() == 'mobile phone is turned off'
    assert mobile_2.turn_off() == 'mobile phone is turned off'
    print(mobile_1.turn_on())
    print(mobile_2.turn_on())
    print(mobile_1.call('555-34343'))
    print(mobile_1.turn_off())
    print(mobile_2.turn_off())
