"""
1.1.1.6 Classes, Instances, Attributes, Methods — the LAB
https://edube.org/learn/python-advanced-1/classes-instances-attributes-methods-the-lab
create a class representing a mobile phone;
your class should implement the following methods:
    __init__ expects a number to be passed as an argument;
    this method stores the number in an instance variable self.number
    turn_on() should return the message 'mobile phone {number} is turned on'.
    Curly brackets are used to mark the place to insert the object's number variable;
    turn_off() should return the message 'mobile phone is turned off';
    call(number) should return the message 'calling {number}'.
    Curly brackets are used to mark the place to insert the object's number variable;
create two objects representing two different mobile phones; assign any random phone numbers to them;
implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
turn off both mobiles.
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
