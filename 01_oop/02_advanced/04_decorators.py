"""
2.4.1.7 Lab – timestamping logger
https://edube.org/learn/python-advanced-1/lab-timestamping-logger
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
