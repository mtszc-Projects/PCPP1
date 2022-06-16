"""
2.4.1.7 Lab – timestamping logger
https://edube.org/learn/python-advanced-1/lab-timestamping-logger
Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds,
eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
"""
from datetime import datetime


def time_decorator(function):
    def wrapper(*args):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return function(*args)
    return wrapper


@time_decorator
def adding(a, b):
    return a + b


@time_decorator
def subtracting(a, b):
    return a - b


if __name__ == "__main__":
    print(adding(5, 10))
    print(subtracting(235, 345))
